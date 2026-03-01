"""
Train the Medical AI Chatbot model using TF-IDF + Cosine Similarity.
Run: python train.py
Saves models to ./models/
"""
import os, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from knowledge_base import INTENTS

os.makedirs("models", exist_ok=True)

corpus, tags = [], []
for intent in INTENTS:
    for pattern in intent["patterns"]:
        corpus.append(pattern.lower())
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer(
    analyzer="char_wb",
    ngram_range=(2, 4),
    max_features=10000,
    sublinear_tf=True,
)
X = vectorizer.fit_transform(corpus)

intent_map = {i["tag"]: i["responses"] for i in INTENTS}

joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump({"corpus": corpus, "tags": tags, "X": X, "intent_map": intent_map, "fallback": "fallback"}, "models/chatbot.pkl")

print(f"✅ Trained on {len(corpus)} patterns across {len(intent_map)} intents.")
print("   models/vectorizer.pkl  ✓")
print("   models/chatbot.pkl     ✓")
