from __future__ import annotations

import shutil
from pathlib import Path

try:
    import whisper
except ImportError:  # pragma: no cover - exercised only when dependency is missing.
    whisper = None


def transcribe_audio_file(audio_path: str | Path, model_name: str = "base") -> str:
    """Return the transcript for the supplied audio file."""
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if whisper is None:
        raise RuntimeError("openai-whisper is not installed. Run pip install -r requirements.txt.")

    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "FFmpeg is not installed or not on PATH. Install FFmpeg and restart the backend before transcribing audio."
        )

    model = whisper.load_model(model_name)
    result = model.transcribe(str(audio_path), fp16=False)
    transcript = result.get("text", "").strip()

    if not transcript:
        raise ValueError("No speech detected in the uploaded audio file.")

    return transcript
