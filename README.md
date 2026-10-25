# VideoInsight AI — Video Knowledge Assistant

Production-oriented AI Video Knowledge Assistant that converts video/audio transcripts into searchable knowledge, structured summaries, action items, decisions, and grounded Q&A.

## Features
- Video/audio upload workflow
- Local Whisper transcription adapter
- Transcript cleaning and chunking
- TF-IDF retrieval for grounded Q&A
- Structured meeting/video insights
- Optional OpenAI-powered summarization and Q&A
- Streamlit dashboard
- CLI-friendly core modules
- Demo transcript
- Unit tests
- No Docker
- No secrets committed

## Architecture
Video/Audio → Transcription → Transcript Processing → Chunking → Retrieval → Grounded Q&A
                                      └→ Summary / Actions / Decisions / Questions

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

FFmpeg is recommended for audio/video conversion. Whisper is optional; the app can also accept a `.txt` transcript for lightweight testing.

This is an independent implementation inspired by the high-level video-assistant problem space. It is not a copy of the reference repository.
