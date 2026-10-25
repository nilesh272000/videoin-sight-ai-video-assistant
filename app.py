import os
import tempfile
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from core.pipeline import build_insights, answer_question
from core.transcriber import transcribe_media

load_dotenv()
st.set_page_config(page_title="VideoInsight AI", page_icon="🎬", layout="wide")
st.title("🎬 VideoInsight AI")
st.caption("Turn videos and meetings into searchable, actionable knowledge")

uploaded = st.file_uploader("Upload a video/audio file or transcript", type=["mp4","mp3","wav","m4a","webm","txt"])

if uploaded:
    suffix = Path(uploaded.name).suffix.lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
        f.write(uploaded.getbuffer())
        path = f.name
    with st.spinner("Processing content..."):
        transcript = transcribe_media(path)
        insights = build_insights(transcript)
    st.session_state["transcript"] = transcript
    st.session_state["insights"] = insights
    st.success("Content processed.")

if "insights" in st.session_state:
    insights = st.session_state["insights"]
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Summary")
        st.write(insights["summary"])
        st.subheader("Key Decisions")
        for x in insights["decisions"]: st.write("• ", x)
    with c2:
        st.subheader("Action Items")
        for x in insights["action_items"]: st.write("• ", x)
        st.subheader("Open Questions")
        for x in insights["open_questions"]: st.write("• ", x)

    st.divider()
    st.subheader("💬 Ask the Video")
    q = st.text_input("Ask a question about the uploaded content")
    if q:
        with st.spinner("Retrieving relevant transcript context..."):
            result = answer_question(q, st.session_state["transcript"])
        st.write(result["answer"])
        with st.expander("Retrieved evidence"):
            for chunk in result["evidence"]: st.write("—", chunk)
