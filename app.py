"""
MedBot — Standalone Medical AI Chatbot Flask App
Run: python app.py
"""
import os, random, joblib, numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

# ── Load trained model ────────────────────────────────────────────────────────
vectorizer = joblib.load(os.path.join(BASE, "models", "vectorizer.pkl"))
data       = joblib.load(os.path.join(BASE, "models", "chatbot.pkl"))

THRESHOLD = 0.15

def get_response(user_input: str) -> str:
    vec  = vectorizer.transform([user_input.lower()])
    sims = cosine_similarity(vec, data["X"]).flatten()
    idx  = int(np.argmax(sims))
    tag  = data["tags"][idx] if sims[idx] >= THRESHOLD else data["fallback"]
    return random.choice(data["intent_map"][tag])

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
def api_chat():
    msg = (request.get_json() or {}).get("message", "").strip()
    if not msg:
        return jsonify({"response": "Please type a medical question."})
    return jsonify({"response": get_response(msg)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
