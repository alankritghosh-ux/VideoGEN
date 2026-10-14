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
cuts on the same shot gives the jump-cut "punch-in" look. Audio gets 15 ms fades at every cut
so joins don't click.

Prints the output-timeline start of every segment (handy for placing overlays) and writes it to
<out>.timeline.json.
"""
import argparse
import json
import subprocess
from pathlib import Path

W, H = 1080, 1920
FADE = 0.015


def crop_expr(zoom: float, cx: float, cy: float, sw: int, sh: int) -> str:
    cw, ch = round(sw / zoom / 2) * 2, round(sh / zoom / 2) * 2
    x = min(max(cx * sw - cw / 2, 0), sw - cw)
    y = min(max(cy * sh - ch / 2, 0), sh - ch)
    return f"crop={cw}:{ch}:{x:.0f}:{y:.0f},scale={W}:{H}:flags=lanczos"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edl", type=Path)
    ap.add_argument("out", type=Path)
    args = ap.parse_args()

    edl = json.loads(args.edl.read_text())
    src, fps = edl["source"], edl.get("fps", 30)
    sw, sh = map(int, subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", src],
        check=True, capture_output=True, text=True,
    ).stdout.strip().split(","))

    parts, labels, timeline, t = [], [], [], 0.0
    for i, s in enumerate(edl["segments"]):
        d = s["out"] - s["in"]
        vf = crop_expr(s.get("zoom", 1.0), s.get("cx", 0.5), s.get("cy", 0.5), sw, sh)
        parts.append(f"[0:v]trim={s['in']}:{s['out']},setpts=PTS-STARTPTS,{vf},setsar=1,fps={fps}[v{i}]")
        parts.append(
            f"[0:a]atrim={s['in']}:{s['out']},asetpts=PTS-STARTPTS,"
            f"afade=t=in:d={FADE},afade=t=out:st={d - FADE:.3f}:d={FADE}[a{i}]"
        )
        labels.append(f"[v{i}][a{i}]")
        timeline.append({"start": round(t, 3), "dur": round(d, 3), "src_in": s["in"], "note": s.get("note", "")})
        t += d
    parts.append(f"{''.join(labels)}concat=n={len(labels)}:v=1:a=1[v][a]")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", ";".join(parts), "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(args.out)],
        check=True,
    )
    Path(f"{args.out}.timeline.json").write_text(json.dumps(timeline, indent=1))
    for seg in timeline:
        print(f"{seg['start']:7.2f}s  +{seg['dur']:5.2f}  (src {seg['src_in']:6.2f})  {seg['note']}")
    print(f"total {t:.2f}s -> {args.out}")


if __name__ == "__main__":
    main()
