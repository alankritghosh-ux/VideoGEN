# VideoGEN

Turns large, unlabelled piles of raw footage into short vertical reels (9:16, 1080x1920).

## Setup

A SessionStart hook (`.claude/settings.json`) runs `scripts/setup.sh` automatically (idempotent, ~1.3 GB of models,
a few minutes on a fresh container). If something is missing, run it by hand, then `scripts/smoke_test.sh` to confirm everything works. Activate Python with `source .venv/bin/activate`.

Cloud-sandbox network rules that shape tool choices:
- HuggingFace, download.pytorch.org, openaipublic (OpenAI Whisper/CLIP), jsdelivr/unpkg, remotion.media are **blocked**.
- PyPI, npm, `git clone` from GitHub, GitHub release assets and storage.googleapis.com work.
- So: no faster-whisper / whisper.cpp / whisperX / openai-whisper. Use `tools/transcribe.py` (sherpa-onnx) instead,
  even when a skill says to run `whisper`.
- CPU only (4 cores, no GPU). Prefer ffmpeg filters over frame-by-frame Python; render Remotion only for motion graphics.

## Layout

- `tools/transcribe.py` — offline word-level ASR. `--model parakeet` (default, 25 EU languages incl. English),
  `sensevoice` (zh/en/ja/ko/yue), `whisper` (any language, segment timing only). Outputs whisper-style JSON
  (works with clipify's `build_ass.py`), `@remotion/captions` JSON and SRT.
- `docs/STYLE.md` — **Campus Fund house style** (read before editing any reel): formats, hook/caption/stamp/quote-card/end-card
  spec, titles and descriptions. Target is YouTube Shorts (same master is used for Instagram Reels, @campus.fund).
- `remotion/` — Remotion 4 project. Composition `Reel` (`src/Reel.tsx`, brand tokens in `src/brand.ts`) implements the house
  style: hook (box/stamp), name lower-third, magenta active-word captions, emphasis stamps, quote cards, end card. Put clips in `remotion/public/clips/`, render with
  `cd remotion && npx remotion render src/index.ts Reel out/x.mp4 --props=props.json`.
- `models/` (gitignored) — sherpa-onnx ASR models, Silero VAD, MediaPipe face detectors, RNNoise `.rnnn` files.
- `.claude/skills/` — vendored skills: Remotion (official), ffmpeg core/effects/social/python + viral-video
  (JosiahSiegel, MIT), clipify (MIT). See `docs/TOOLS.md`.
- Never commit media (`input/`, `work/`, `output/` are gitignored).

## Reel delivery spec

H.264 High, yuv420p, 1080x1920, 30 fps, `-crf 18 -movflags +faststart`, AAC 48 kHz, loudness -14 LUFS / -1 dBTP
(`ffmpeg-normalize -nt ebu -t -14 -tp -1` or `loudnorm=I=-14:TP=-1`). Keep captions/graphics out of the bottom
~20% and top ~12% (platform UI).

## Licensing

Remotion is source-available; we qualify for the free license (confirmed 2026-10-14). Everything else installed is MIT/BSD/Apache/ISC/Unlicense.
