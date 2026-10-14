#!/usr/bin/env bash
# End-to-end check of the toolchain on a synthetic clip. Usage: scripts/smoke_test.sh
set -euo pipefail
cd "$(dirname "$0")/.."
source .venv/bin/activate
W=$(mktemp -d)
trap 'rm -rf "$W"' EXIT
ok() { echo "  ok  $*"; }

# 1. synthetic 16:9 clip with speech (Parakeet's bundled English sample)
ffmpeg -v error -f lavfi -i testsrc2=s=1280x720:r=30 -i models/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8/test_wavs/en.wav \
  -shortest -c:v libx264 -pix_fmt yuv420p -c:a aac "$W/in.mp4"; ok "ffmpeg synth"
python tools/transcribe.py "$W/in.mp4" --out "$W/t" 2>/dev/null
python -c "import json,sys; c=json.load(open('$W/t.captions.json')); assert len(c)>3, c; print('  ok  transcribe:', ''.join(x['text'] for x in c))"
scenedetect -q -i "$W/in.mp4" -o "$W" detect-adaptive list-scenes -q >/dev/null; ok "scenedetect"
auto-editor "$W/in.mp4" --no-open -o "$W/cut.mp4" >/dev/null 2>&1; ok "auto-editor"
python .claude/skills/clipify/scripts/build_ass.py "$W/t.whisper.json" "$W/t.ass" >/dev/null
ffmpeg -v error -i "$W/in.mp4" -vf "crop=ih*9/16:ih,scale=1080:1920,ass=$W/t.ass" \
  -af "arnndn=m=models/rnnnoise/std.rnnn,loudnorm=I=-14:TP=-1" -c:v libx264 -preset ultrafast "$W/reel.mp4"; ok "9:16 crop + ASS captions + denoise + loudnorm"
python - "$W/in.mp4" <<'PY' 2>/dev/null
import sys, cv2, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
cap = cv2.VideoCapture(sys.argv[1]); _, frame = cap.read()
opts = vision.FaceDetectorOptions(base_options=BaseOptions(model_asset_path="models/mediapipe/blaze_face_short_range.tflite"))
with vision.FaceDetector.create_from_options(opts) as d:
    d.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
print("  ok  mediapipe face detector")
PY
python -c "import librosa, imagehash, moviepy, noisereduce, av; print('  ok  python imports')"
mkdir -p remotion/public/clips && cp "$W/reel.mp4" remotion/public/clips/_smoke.mp4
python -c "import json; json.dump({'clip':'clips/_smoke.mp4','durationSec':1,'hook':'smoke','captions':json.load(open('$W/t.captions.json'))}, open('$W/props.json','w'))"
(cd remotion && npx remotion render src/index.ts Reel "$W/remotion.mp4" --props="$W/props.json" --log=error >/dev/null)
rm remotion/public/clips/_smoke.mp4; ok "remotion render"
echo "all good"
