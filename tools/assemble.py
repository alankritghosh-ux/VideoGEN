#!/usr/bin/env python3
"""Cut + reframe a 1080x1920 clip from an edit decision list (EDL), in one ffmpeg pass.

EDL JSON:
{
  "source": "input/x.mp4",
  "fps": 30,
  "segments": [
    {"in": 49.70, "out": 53.40, "zoom": 1.0, "cx": 0.5, "cy": 0.36, "note": "cold open"},
    ...
  ]
}
zoom >= 1 punches in around (cx, cy) (fractions of the source frame); alternating zooms between
cuts on the same shot gives the jump-cut "punch-in" look. Optional per segment:
  "punch_from": 1.4   start wider-zoomed and ease into `zoom` over 0.25 s (impact on a cut)
  "fade_out": 0.08    longer audio fade-out (s) when a word's tail runs into the cut
  "freeze_at": 53.16  hold this source frame for the segment's length (audio still plays in..out),
                      pushing in from `zoom` to `zoom_to`: a beat to let a line land
  "zoom_to", "cx_to", "cy_to"   drift linearly from zoom/cx/cy to these over the segment (slow push-in,
                      pan that keeps the face centred); combine with `punch_from` if wanted
  "cx_keys": [[t, cx], ...]   piecewise-linear pan through source-time keyframes instead of cx/cx_to
                      (two keys 1 frame apart make a step: re-centre on the source's own cut). cy_keys likewise
  "dissolve": 0.2     cross-dissolve (s) from the previous segment into this one, with a matching audio
                      crossfade. 0/absent = hard cut (audio still gets 15 ms fades so joins don't click)
Audio past the end of the source is padded with silence, so a freeze may run beyond the file.

Each segment is rendered to an intermediate (in parallel, input-seeked so nothing is decoded twice), then the
intermediates are chained. Prints the output-timeline start of every segment (handy for placing overlays) and
writes it to <out>.timeline.json.
"""
import argparse
import json
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

W, H = 1080, 1920
FADE = 0.015


def crop_expr(zoom: float, cx: float, cy: float, sw: int, sh: int) -> str:
    cw, ch = round(sw / zoom / 2) * 2, round(sh / zoom / 2) * 2
    x = min(max(cx * sw - cw / 2, 0), sw - cw)
    y = min(max(cy * sh - ch / 2, 0), sh - ch)
    return f"crop={cw}:{ch}:{x:.0f}:{y:.0f},scale={W}:{H}:flags=lanczos"


def motion_expr(s: dict, sw: int, sh: int, src_fps: float) -> str:
    """zoompan-based crop with per-frame zoom (punch-in ease and/or linear drift) and a linear pan."""
    z0, z1 = s.get("zoom", 1.0), s.get("zoom_to", s.get("zoom", 1.0))
    frames = max(1, round((s["out"] - s["in"]) * src_fps))
    base = max(W / sw, H / sh)
    u = f"(on/{max(frames - 1, 1)})"  # 0..1 across the segment
    zexpr = f"({z0}+({z1}-{z0})*{u})"
    if "punch_from" in s:
        n = max(1, round(0.25 * src_fps))
        zexpr = f"({zexpr}+({s['punch_from']}-{z0})*pow(max(0\\,1-on/{n})\\,2))"
    def track(axis: str) -> str:
        keys = s.get(f"{axis}_keys")
        if not keys:
            c0, c1 = s.get(axis, 0.5), s.get(f"{axis}_to", s.get(axis, 0.5))
            return f"({c0}+({c1}-{c0})*{u})"
        # Additive piecewise-linear form: v0 + sum slope_i * clip(on - f_i, 0, f_i+1 - f_i).
        pts = [((t - s["in"]) * src_fps, v) for t, v in keys]
        expr = f"{pts[0][1]}"
        for (f0, v0), (f1, v1) in zip(pts, pts[1:]):
            if f1 > f0:
                expr += f"+({(v1 - v0) / (f1 - f0):.6f})*clip(on-{f0:.2f}\\,0\\,{f1 - f0:.2f})"
        return f"({expr})"
    x = f"clip(iw*{track('cx')}-iw/zoom/2\\,0\\,iw-iw/zoom)"
    y = f"clip(ih*{track('cy')}-ih/zoom/2\\,0\\,ih-ih/zoom)"
    pre = f"scale={round(sw * base / 2) * 2}:{round(sh * base / 2) * 2}," if base != 1 else ""
    # zoompan reports a bogus EOF timestamp; re-stamp frames and close the stream with trim.
    return (f"{pre}zoompan=z='{zexpr}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={src_fps},"
            f"setpts=N/({src_fps}*TB),trim=end_frame={frames}")


def freeze_expr(s: dict, sw: int, sh: int, src_fps: float) -> str:
    """Single frame held for the segment duration with a linear push-in."""
    d = s["out"] - s["in"]
    frames = max(1, round(d * src_fps))
    z0, z1 = s.get("zoom", 1.0), s.get("zoom_to", s.get("zoom", 1.0))
    base = max(W / sw, H / sh)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    x = f"clip(iw*{s.get('cx', 0.5)}-iw/zoom/2\\,0\\,iw-iw/zoom)"
    y = f"clip(ih*{s.get('cy', 0.5)}-ih/zoom/2\\,0\\,ih-ih/zoom)"
    pre = f"scale={round(sw * base / 2) * 2}:{round(sh * base / 2) * 2}," if base != 1 else ""
    return (f"trim=end_frame=1,setpts=PTS-STARTPTS,{pre}"
            f"zoompan=z='{zexpr}':x='{x}':y='{y}':d={frames}:s={W}x{H}:fps={src_fps},"
            f"setpts=N/({src_fps}*TB),trim=end_frame={frames}")


def render_segment(i: int, s: dict, src: str, fps: int, sw: int, sh: int, src_fps: float, tmp: Path) -> Path:
    d = s["out"] - s["in"]
    if "freeze_at" in s:
        vf, vseek = freeze_expr(s, sw, sh, src_fps), s["freeze_at"]
    elif any(k in s for k in ("punch_from", "zoom_to", "cx_to", "cy_to", "cx_keys", "cy_keys")):
        vf, vseek = motion_expr(s, sw, sh, src_fps), s["in"]
    else:
        vf, vseek = crop_expr(s.get("zoom", 1.0), s.get("cx", 0.5), s.get("cy", 0.5), sw, sh), s["in"]
    fo = s.get("fade_out", FADE)
    out = tmp / f"seg{i:02d}.mkv"
    graph = (f"[0:v]{vf},setsar=1,fps={fps},settb=AVTB,trim=duration={d:.3f}[v];"
             f"[1:a]atrim=duration={d:.3f},asetpts=PTS-STARTPTS,apad=whole_dur={d:.3f},"
             f"afade=t=in:d={FADE},afade=t=out:st={d - fo:.3f}:d={fo}[a]")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", f"{vseek:.3f}", "-t", f"{d + 0.5:.3f}", "-i", src,
         "-ss", f"{s['in']:.3f}", "-t", f"{d:.3f}", "-i", src, "-filter_complex", graph,
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "10", "-preset", "fast", "-pix_fmt", "yuv420p",
         "-c:a", "pcm_s16le", "-ar", "48000", str(out)],
        check=True,
    )
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edl", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()

    edl = json.loads(args.edl.read_text())
    src, fps = edl["source"], edl.get("fps", 30)
    sw, sh, rate = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
         "-of", "csv=p=0", src],
        check=True, capture_output=True, text=True,
    ).stdout.strip().split(",")
    sw, sh = int(sw), int(sh)
    num, den = map(int, rate.split("/"))
    src_fps = num / den
    segs = edl["segments"]

    timeline, t = [], 0.0
    for i, s in enumerate(segs):
        dis = s.get("dissolve", 0) if i else 0
        t -= dis
        timeline.append({"start": round(t, 3), "dur": round(s["out"] - s["in"], 3), "src_in": s["in"],
                         "dissolve": dis, "note": s.get("note", "")})
        t += s["out"] - s["in"]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="assemble_", dir=args.out.parent) as tmpdir:
        tmp = Path(tmpdir)
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            files = list(pool.map(lambda a: render_segment(*a), [(i, s, src, fps, sw, sh, src_fps, tmp) for i, s in enumerate(segs)]))
        # Chain the intermediates: xfade/acrossfade where a dissolve is asked for, concat otherwise.
        # xfade insists on identical timebases, and the mkv intermediates / concat outputs differ: normalise.
        tb = f"settb=AVTB,fps={fps}"
        parts = [f"[{i}:v]{tb}[n{i}]" for i in range(len(segs))]
        vcur, acur, acc = "[n0]", "[0:a]", segs[0]["out"] - segs[0]["in"]
        for i, s in enumerate(segs[1:], start=1):
            d, dis = s["out"] - s["in"], s.get("dissolve", 0)
            if dis > 0:
                parts.append(f"{vcur}[n{i}]xfade=transition=fade:duration={dis}:offset={acc - dis:.3f}[vx{i}]")
                parts.append(f"{acur}[{i}:a]acrossfade=d={dis}:c1=tri:c2=tri[ax{i}]")
                acc += d - dis
            else:
                parts.append(f"{vcur}[n{i}]concat=n=2:v=1:a=0,{tb}[vx{i}]")
                parts.append(f"{acur}[{i}:a]concat=n=2:v=0:a=1[ax{i}]")
                acc += d
            vcur, acur = f"[vx{i}]", f"[ax{i}]"
        parts.append(f"{vcur}null[v];{acur}anull[a]")
        cmd = ["ffmpeg", "-v", "error", "-y"]
        for f in files:
            cmd += ["-i", str(f)]
        cmd += ["-filter_complex", ";".join(parts), "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(args.out)]
        subprocess.run(cmd, check=True)

    Path(f"{args.out}.timeline.json").write_text(json.dumps(timeline, indent=1))
    for seg in timeline:
        x = f" ~{seg['dissolve']:.2f}" if seg.get("dissolve") else "      "
        print(f"{seg['start']:7.2f}s{x} +{seg['dur']:5.2f}  (src {seg['src_in']:6.2f})  {seg['note']}")
    print(f"total {t:.2f}s -> {args.out}")


if __name__ == "__main__":
    main()
