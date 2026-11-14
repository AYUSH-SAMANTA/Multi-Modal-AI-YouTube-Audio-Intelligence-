import os

import requests
import streamlit as st

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.title("Speech-to-Text Demo")
st.caption("Upload a short audio clip and transcribe it using the FastAPI backend.")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a", "ogg", "flac"])

if uploaded_file is not None:
    if st.button("Transcribe"):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type or "application/octet-stream",
            )
        }

        with st.spinner("Transcribing audio..."):
            response = requests.post(f"{API_BASE_URL}/api/transcribe", files=files, timeout=300)

        if response.ok:
            transcript = response.json().get("transcript", "")
            st.success("Transcript")
            st.write(transcript)
        else:
            st.error(f"Request failed: {response.status_code} - {response.text}")
