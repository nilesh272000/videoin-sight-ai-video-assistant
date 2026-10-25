from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def chunks(text: str, size: int = 700):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)] or [text]

def retrieve(query: str, text: str, k: int = 4):
    docs = chunks(text)
    if not docs: return []
    matrix = TfidfVectorizer(stop_words="english").fit_transform(docs + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
    idx = scores.argsort()[::-1][:k]
    return [docs[i] for i in idx if scores[i] > 0]
