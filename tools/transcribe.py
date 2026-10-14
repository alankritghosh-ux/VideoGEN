#!/usr/bin/env python3
"""Offline word-level transcription for any video/audio file (CPU, sherpa-onnx).

Writes next to --out (default: <input>.transcript):
  .whisper.json   whisper-style {"text", "language", "segments":[{start,end,text,words:[{word,start,end}]}]}
                  (drop-in for .claude/skills/clipify/scripts/build_ass.py)
  .captions.json  @remotion/captions Caption[] (for remotion/src/Reel.tsx)
  .srt            plain subtitles

Models (see scripts/setup.sh):
  parakeet   NVIDIA Parakeet-TDT 0.6B v3, 25 European languages, word timestamps (default)
  sensevoice zh/en/ja/ko/yue, token timestamps
  whisper    Whisper small, ~100 languages, segment-level timing only
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import sherpa_onnx

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"
SR = 16000


def load_audio(path: Path) -> np.ndarray:
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
        check=True, capture_output=True,
    ).stdout
    return np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32768.0


def make_recognizer(model: str, threads: int):
    if model == "parakeet":
        d = MODELS / "sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8"
        return sherpa_onnx.OfflineRecognizer.from_transducer(
            encoder=str(d / "encoder.int8.onnx"), decoder=str(d / "decoder.int8.onnx"),
            joiner=str(d / "joiner.int8.onnx"), tokens=str(d / "tokens.txt"),
            model_type="nemo_transducer", num_threads=threads,
        )
    if model == "sensevoice":
        d = MODELS / "sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2025-09-09"
        return sherpa_onnx.OfflineRecognizer.from_sense_voice(
            model=str(d / "model.int8.onnx"), tokens=str(d / "tokens.txt"),
            use_itn=True, num_threads=threads,
        )
    if model == "whisper":
        d = MODELS / "sherpa-onnx-whisper-small"
        return sherpa_onnx.OfflineRecognizer.from_whisper(
            encoder=str(d / "small-encoder.int8.onnx"), decoder=str(d / "small-decoder.int8.onnx"),
            tokens=str(d / "small-tokens.txt"), num_threads=threads, task="transcribe",
        )
    raise SystemExit(f"unknown model {model}")


def speech_segments(audio: np.ndarray, max_sec: float):
    """Split on silence with Silero VAD so long files stay within model limits."""
    cfg = sherpa_onnx.VadModelConfig()
    cfg.silero_vad.model = str(MODELS / "silero_vad.onnx")
    cfg.silero_vad.min_silence_duration = 0.4
    cfg.silero_vad.min_speech_duration = 0.25
    cfg.silero_vad.max_speech_duration = max_sec
    cfg.sample_rate = SR
    vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=max(60, len(audio) / SR + 1))
    win = cfg.silero_vad.window_size
    for i in range(0, len(audio), win):
        vad.accept_waveform(audio[i:i + win])
        while not vad.empty():
            yield vad.front.start / SR, np.array(vad.front.samples, dtype=np.float32)
            vad.pop()
    vad.flush()
    while not vad.empty():
        yield vad.front.start / SR, np.array(vad.front.samples, dtype=np.float32)
        vad.pop()


def tokens_to_words(tokens, stamps, offset: float, seg_end: float):
    """Merge sub-word tokens (leading space / '▁' starts a word) into timed words."""
    words = []
    for tok, ts in zip(tokens, stamps):
        starts_word = tok.startswith((" ", "▁")) or not words
        text = tok.replace("▁", " ")
        if starts_word and text.strip():
            words.append({"word": text.strip(), "start": offset + ts})
        elif words:
            words[-1]["word"] += text.strip()
    for i, w in enumerate(words):
        w["end"] = words[i + 1]["start"] if i + 1 < len(words) else seg_end
        w["start"], w["end"] = round(w["start"], 3), round(min(w["end"], w["start"] + 1.5), 3)
    return words


def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path)
    ap.add_argument("--model", default="parakeet", choices=["parakeet", "sensevoice", "whisper"])
    ap.add_argument("--out", type=Path, help="output path prefix")
    ap.add_argument("--threads", type=int, default=4)
    args = ap.parse_args()

    out = args.out or args.input.with_suffix(".transcript")
    audio = load_audio(args.input)
    rec = make_recognizer(args.model, args.threads)
    # Whisper's encoder window is 30 s; the others handle longer chunks fine.
    max_sec = 28 if args.model == "whisper" else 60

    segments, language = [], ""
    for start, samples in speech_segments(audio, max_sec):
        s = rec.create_stream()
        s.accept_waveform(SR, samples)
        rec.decode_stream(s)
        r = s.result
        text = r.text.strip()
        if not text:
            continue
        end = start + len(samples) / SR
        language = language or getattr(r, "lang", "")
        words = tokens_to_words(r.tokens, r.timestamps, start, end) if len(r.timestamps) else [
            {"word": text, "start": round(start, 3), "end": round(end, 3)}
        ]
        segments.append({"start": round(start, 3), "end": round(end, 3), "text": text, "words": words})
        print(f"[{start:7.2f}] {text}", file=sys.stderr)

    whisper_json = {"text": " ".join(s["text"] for s in segments), "language": language, "segments": segments}
    Path(f"{out}.whisper.json").write_text(json.dumps(whisper_json, ensure_ascii=False, indent=1))

    captions = [
        {"text": (" " if i else "") + w["word"], "startMs": int(w["start"] * 1000), "endMs": int(w["end"] * 1000),
         "timestampMs": int(w["start"] * 1000), "confidence": None}
        for i, w in enumerate(w for s in segments for w in s["words"])
    ]
    Path(f"{out}.captions.json").write_text(json.dumps(captions, ensure_ascii=False))

    with open(f"{out}.srt", "w") as f:
        for i, s in enumerate(segments, 1):
            f.write(f"{i}\n{srt_time(s['start'])} --> {srt_time(s['end'])}\n{s['text']}\n\n")
    print(f"wrote {out}.whisper.json / .captions.json / .srt ({len(segments)} segments)", file=sys.stderr)


if __name__ == "__main__":
    main()
