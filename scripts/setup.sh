#!/usr/bin/env bash
# Idempotent environment setup: Python venv, Remotion deps, offline models.
# Every model comes from GitHub releases / git or storage.googleapis.com, because
# HuggingFace is blocked in the cloud sandbox. Safe to re-run; skips what exists.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD
M="$ROOT/models"
ASR=https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models
MP=https://storage.googleapis.com/mediapipe-models/face_detector

log() { echo "[setup] $*" >&2; }

# System libs: libass is in Ubuntu's ffmpeg; mediapipe needs EGL.
if ! ldconfig -p | grep -q libEGL.so.1 && command -v apt-get >/dev/null; then
  log "installing libegl1"
  (apt-get install -y -q libegl1 >/dev/null 2>&1 || { apt-get update -q >/dev/null && apt-get install -y -q libegl1 >/dev/null; }) || log "WARN: libegl1 install failed (mediapipe reframing unavailable)"
fi

if [ ! -x .venv/bin/python ]; then
  log "creating .venv (python 3.12)"
  uv venv .venv --python 3.12 -q
fi
log "python deps"
VIRTUAL_ENV="$ROOT/.venv" uv pip install -q -r requirements.txt

if [ ! -d remotion/node_modules ]; then
  log "remotion npm deps"
  (cd remotion && npm ci --silent)
fi

mkdir -p "$M/mediapipe" "$M/rnnnoise"
fetch_tar() { # name
  [ -d "$M/$1" ] && return
  log "downloading $1"
  curl -fsSL "$ASR/$1.tar.bz2" | tar xj -C "$M"
}
fetch_tar sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8
fetch_tar sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2025-09-09
if [ ! -d "$M/sherpa-onnx-whisper-small" ]; then
  fetch_tar sherpa-onnx-whisper-small
  rm -f "$M"/sherpa-onnx-whisper-small/small-{encoder,decoder}.onnx  # keep int8 only
fi
[ -f "$M/silero_vad.onnx" ] || curl -fsSLo "$M/silero_vad.onnx" "$ASR/silero_vad.onnx"

for f in blaze_face_short_range blaze_face_full_range; do
  [ -f "$M/mediapipe/$f.tflite" ] || curl -fsSLo "$M/mediapipe/$f.tflite" "$MP/$f/float16/latest/$f.tflite"
done

if [ ! -f "$M/rnnnoise/std.rnnn" ]; then
  log "rnnoise models"
  tmp=$(mktemp -d)
  git clone -q --depth 1 https://github.com/richardpl/arnndn-models "$tmp/arnndn"
  cp "$tmp"/arnndn/*.rnnn "$M/rnnnoise/"
  rm -rf "$tmp"
fi

log "done ($(du -sh "$M" | cut -f1) of models)"
