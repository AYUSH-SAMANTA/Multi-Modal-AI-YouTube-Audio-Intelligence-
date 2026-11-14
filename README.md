# Speech-to-Text Project

This project provides a small speech-to-text application using FastAPI for the API and Streamlit for the UI.

## Features

- FastAPI backend for uploading audio and returning a transcript
- Streamlit frontend for a simple browser interface
- Environment-based configuration with `.env`
- Whisper-based transcription using the packages in `requirements.txt`

## Project structure

- `app/config.py` – configuration settings
- `app/transcriber.py` – Whisper transcription logic
- `app/main.py` – FastAPI endpoints
- `streamlit_app.py` – Streamlit frontend
- `tests/test_app.py` – smoke tests for the API

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Start the API:
   `uvicorn app.main:app --reload`
4. In a second terminal, start the frontend:
   `streamlit run streamlit_app.py`

## Environment variables

- `GEMINI_API_KEY` – kept in the workspace `.env` file for future integrations
- `API_BASE_URL` – used by the Streamlit frontend, defaulting to `http://localhost:8000`
- `MODEL_NAME` – optional Whisper model override, default `base`

## Notes

The API accepts uploaded audio files and returns a transcript as JSON. It expects a short audio file in a common format such as WAV, MP3, M4A, OGG, or FLAC.
