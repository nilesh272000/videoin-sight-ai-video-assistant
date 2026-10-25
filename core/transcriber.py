from pathlib import Path

def transcribe_media(path: str) -> str:
    p = Path(path)
    if p.suffix.lower() == ".txt":
        return p.read_text(encoding="utf-8")
    try:
        import whisper
        model_name = __import__("os").getenv("WHISPER_MODEL", "base")
        model = whisper.load_model(model_name)
        result = model.transcribe(str(p), fp16=False)
        return result.get("text", "").strip()
    except Exception as exc:
        return f"Transcription unavailable. Please upload a transcript (.txt) or install/configure Whisper and FFmpeg. Detail: {exc}"
