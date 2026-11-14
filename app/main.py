from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, File, HTTPException, UploadFile

from app.config import get_settings
from app.transcriber import transcribe_audio_file

app = FastAPI(title=get_settings().app_name)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Speech-to-text API is running."}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "speech_to_text_api"}


@app.post("/api/transcribe")
async def transcribe(file: UploadFile = File(...)) -> dict[str, str]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file name supplied.")

    name = Path(file.filename)
    suffix = name.suffix or ".wav"

    with NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(await file.read())

    try:
        transcript = transcribe_audio_file(temp_path, model_name=get_settings().model_name)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - thin wrapper around external dependency failures.
        raise HTTPException(status_code=500, detail=f"Transcription failed: {exc}") from exc
    finally:
        temp_path.unlink(missing_ok=True)

    return {"transcript": transcript}
