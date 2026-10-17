#!/usr/bin/env python3
"""Re-time a source transcript onto an assembled cut.

    python tools/edl_captions.py edits/x/edl.json work/x/cut.mp4.timeline.json work/src.whisper.json out.captions.json

Reads the whisper-style word list produced by tools/transcribe.py for the *source* file, keeps the words that
fall inside each EDL segment, shifts them onto the output timeline written by tools/assemble.py, and writes a
@remotion/captions Caption[] (for Reel / Lore). Fillers ("uh", "um", "er" and single stray letters) are dropped
from the captions; the audio keeps them.
"""
import json
import re
import sys
from pathlib import Path

FILLER = re.compile(r"^[\W_]*(uh+|um+|er+|hmm|mm|[b-hj-z])[\W_]*$", re.I)  # keeps "a" and "I"


def main(edl_path, timeline_path, whisper_path, out_path):
    edl = json.loads(Path(edl_path).read_text())
    timeline = json.loads(Path(timeline_path).read_text())
    words = [w for seg in json.loads(Path(whisper_path).read_text())["segments"] for w in seg["words"]]
    caps = []
    for s, t in zip(edl["segments"], timeline):
        if "freeze_at" in s:
            continue
        for w in words:
            mid = (w["start"] + w["end"]) / 2
            if s["in"] <= mid < s["out"] and not FILLER.match(w["word"]):
                start = max(w["start"], s["in"]) - s["in"] + t["start"]
                end = min(w["end"], s["out"]) - s["in"] + t["start"]
                caps.append({"text": (" " if caps else "") + w["word"].strip(), "startMs": round(start * 1000),
                             "endMs": round(end * 1000), "timestampMs": None, "confidence": None})
    Path(out_path).write_text(json.dumps(caps, indent=1))
    print(f"{len(caps)} words -> {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
