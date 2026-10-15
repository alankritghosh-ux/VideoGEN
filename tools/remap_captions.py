#!/usr/bin/env python3
"""Re-time @remotion/captions JSON (source timeline) onto the cut produced by tools/assemble.py.

    python tools/remap_captions.py work/x/tr.captions.json work/x/cut.mp4.timeline.json out.json [--fix fixes.json]

Words whose midpoint falls outside every kept segment are dropped; the rest are shifted to the
output timeline and clamped to their segment. `fixes.json` is {"<source startMs>": "new text"}
for ASR misreads ("Synputer" -> " Simputer"); an empty string drops the word.
"""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("captions", type=Path)
    ap.add_argument("timeline", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--fix", type=Path)
    a = ap.parse_args()
    caps = json.loads(a.captions.read_text())
    segs = json.loads(a.timeline.read_text())
    fixes = json.loads(a.fix.read_text()) if a.fix else {}
    out = []
    for c in caps:
        txt = fixes.get(str(c["startMs"]), c["text"])
        if txt == "":
            continue
        mid = (c["startMs"] + c["endMs"]) / 2000
        for s in segs:
            if s["src_in"] <= mid < s["src_in"] + s["dur"]:
                off = s["start"] - s["src_in"]
                lo, hi = s["start"] * 1000, (s["start"] + s["dur"]) * 1000
                st = round(min(max(c["startMs"] + off * 1000, lo), hi))
                en = round(min(max(c["endMs"] + off * 1000, lo), hi))
                out.append({**c, "text": txt, "startMs": st, "endMs": max(en, st + 40), "timestampMs": st})
                break
    out.sort(key=lambda c: c["startMs"])
    a.out.write_text(json.dumps(out, indent=1))
    print(f"{len(out)}/{len(caps)} words kept -> {a.out}")


if __name__ == "__main__":
    main()
