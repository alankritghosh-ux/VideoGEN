# Toolchain for footage → reels

Researched and verified in the cloud sandbox on 2026-10-14 (CPU only; HuggingFace blocked).
✅ = installed and covered by `scripts/smoke_test.sh`.

## Installed

| Stage | Tool | License | Notes |
|---|---|---|---|
| Transcription | ✅ **sherpa-onnx** 1.13.8 + Parakeet-TDT 0.6B v3 int8 | Apache-2.0 / CC-BY-4.0 | Word timestamps; ~12× realtime on 4 CPU cores; 25 European languages |
| | ✅ SenseVoice int8 (2025-09-09) | Apache-2.0 | zh/en/ja/ko/yue, fastest |
| | ✅ Whisper small int8 (ONNX) | MIT | ~100 languages, segment timing only |
| | ✅ Silero VAD | MIT | Speech chunking inside `tools/transcribe.py` |
| Shot detection | ✅ PySceneDetect 0.7.2 | BSD-3 | `detect-adaptive`; split long footage into shots |
| Auto-cutting | ✅ auto-editor 29.3.1 | Unlicense | Silence/motion cuts; exports Premiere/Resolve/FCP/Shotcut XML |
| Reframe 9:16 | ✅ MediaPipe 1.1.0 + BlazeFace short/full range | Apache-2.0 | Face-tracked crop; needs `libegl1` |
| Decode / compose | ✅ ffmpeg 6.1 (libass, lut3d, arnndn, loudnorm, vidstab, scdet), PyAV 19, MoviePy 2.2, OpenCV 5 | LGPL/GPL, BSD, MIT, Apache | |
| Captions | ✅ ASS via clipify `build_ass.py` + libass burn-in; pysubs2 | MIT | Cheapest high-quality karaoke captions on CPU |
| Motion graphics | ✅ **Remotion 4.0.535** (+captions, transitions, media, google-fonts) | Source-available ⚠️ | Uses preinstalled Chromium headless shell (remotion.media blocked). ~10 fps render on CPU |
| Audio finishing | ✅ ffmpeg `arnndn` + RNNoise models (richardpl/arnndn-models), noisereduce 3.0.3, ffmpeg-normalize 1.43 | BSD/MIT | Denoise speech, -14 LUFS |
| Music sync | ✅ librosa 1.0 | ISC | `beat_track` / `onset_detect` for beat-synced cuts |
| Dedup / quality | ✅ imagehash 4.3.2, OpenCV Laplacian, ffmpeg `blurdetect`/`signalstats`/`blackdetect`/`freezedetect` | BSD | Drop duplicate, blurry, dark shots |
| Fetch | ✅ yt-dlp | Unlicense | |

## Vendored Claude skills (`.claude/skills/`)

| Source | Skills |
|---|---|
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | remotion-best-practices (router), -create, -markup (transitions, cropping, light leaks, motion blur, sfx, audio viz…), -captions, -multimedia, -render, -studio, -docs |
| [JosiahSiegel/claude-plugin-marketplace](https://github.com/JosiahSiegel/claude-plugin-marketplace) (MIT) | ffmpeg-core: audio-processing, captions-subtitles, command-syntax, filter-complex-patterns, noise-reduction, stabilization-360, video-analysis, … · ffmpeg-effects: karaoke-animated-text, kinetic-captions, color-grading-chromakey, transitions-effects, glitch, shapes, waveforms · ffmpeg-social-video: viral-video-animated-captions, hook-templates, platform-specs · ffmpeg-python: opencv/pyav integration · viral-video-master: short-form, hooks-retention, platform-algorithms |
| [louisedesadeleer/clipify](https://github.com/louisedesadeleer/clipify) (MIT) | Find moments (dialogue or action/transients), cut, face-pan 9:16, opus-style captions |

Overrides: these skills mention `whisper` / `@remotion/whisper-webgpu` / `-hwaccel videotoolbox`. In this repo use
`tools/transcribe.py` and plain software decode instead.

## Evaluated, not installed

| Tool | Why not |
|---|---|
| faster-whisper, whisper.cpp, whisperX, openai-whisper, Vosk | Weights only on HF / blocked hosts |
| ClipsAI | Depends on whisperX + pyannote (HF); stale since 2024 |
| AI-Youtube-Shorts-Generator, hotclip, openshorts | Reference designs; need OpenAI keys / Whisper. Our pipeline reproduces them with Claude as the highlight ranker |
| Revideo (MIT) | Good Remotion alternative if licensing is a problem; not needed while Remotion is allowed |
| Motion Canvas, editly, FFCreator | Editor-centric or need headless-gl/xvfb |
| madmom, essentia, aubio | NC model license / AGPL / no py3.13 wheel |
| CLIP semantic search (open_clip RN50 from GitHub releases, SigLIP from GCS) | Feasible, but needs torch (multi-GB CUDA wheels from PyPI) or ONNX export. Add when indexing needs semantic tags |
| TransNetV2 | Neural shot detection; weights cloneable from GitHub. Add if PySceneDetect misses soft cuts |
| MLT `melt` / Shotcut, Kdenlive, Olive | Only needed for human-editable project handoff; auto-editor already exports Shotcut XML |
