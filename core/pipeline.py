import os
import re
from .retriever import retrieve

def _llm(prompt: str):
    key = os.getenv("OPENAI_API_KEY")
    if not key: return None
    try:
        from openai import OpenAI
        client = OpenAI(api_key=key)
        r = client.chat.completions.create(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), messages=[{"role":"user","content":prompt}], temperature=0.2)
        return r.choices[0].message.content
    except Exception:
        return None

def build_insights(text: str):
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    summary = _llm("Summarize this transcript in 5 concise bullets:\n" + text[:12000])
    if not summary: summary = "\n".join("• " + s for s in sentences[:5]) or "No transcript content available."
    actions = [s for s in sentences if any(x in s.lower() for x in ["will ", "should ", "action", "todo", "follow up", "deadline"])]
    decisions = [s for s in sentences if any(x in s.lower() for x in ["decided", "decision", "agreed", "approved"])]
    questions = [s for s in sentences if "?" in s]
    return {"summary": summary, "action_items": actions[:8], "decisions": decisions[:8], "open_questions": questions[:8]}

def answer_question(question: str, transcript: str):
    evidence = retrieve(question, transcript)
    context = "\n\n".join(evidence)
    answer = _llm(f"Answer only from the transcript context. If the answer is not supported, say so.\nQuestion: {question}\nContext:\n{context}")
    if not answer:
        answer = evidence[0] if evidence else "I could not find supporting evidence in the transcript."
    return {"answer": answer, "evidence": evidence}
