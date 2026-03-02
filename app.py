"""
MedBot — Medical AI Chatbot Flask App
Uses ML-trained classifier (SVM / Naive Bayes / Logistic Regression)
Routes:
  GET  /           → Landing page
  GET  /chat       → Chat interface (with voice assistant)
  POST /api/chat   → JSON: {"message": "..."} → {"response": "...", "intent": "...", "confidence": 0.95}
  GET  /api/models → Returns model accuracy comparison
"""
import os, random, json, joblib
from flask import Flask, render_template, request, jsonify

app    = Flask(__name__)
BASE   = os.path.dirname(os.path.abspath(__file__))

def load(name):
    return joblib.load(os.path.join(BASE, "models", name))

# ── Load ML models ────────────────────────────────────────────────────────────
best_model    = load("best_model.pkl")
label_encoder = load("label_encoder.pkl")
knowledge     = load("knowledge.pkl")

with open(os.path.join(BASE, "models", "model_meta.json")) as f:
    model_meta = json.load(f)

CONFIDENCE_THRESHOLD = 0.30   # below this → fallback

def predict(user_input: str) -> dict:
    """Run ML inference and return intent + response + confidence."""
    text    = [user_input.lower().strip()]
    proba   = best_model.predict_proba(text)[0]
    top_idx = int(proba.argmax())
    conf    = float(proba[top_idx])
    tag     = label_encoder.inverse_transform([top_idx])[0]

    if conf < CONFIDENCE_THRESHOLD:
        tag = knowledge["fallback"]

    responses = knowledge["intent_map"].get(tag, knowledge["intent_map"][knowledge["fallback"]])
    return {
        "response":   random.choice(responses),
        "intent":     tag,
        "confidence": round(conf * 100, 1),
    }

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", meta=model_meta)

@app.route("/chat")
def chat():
    return render_template("chat.html", meta=model_meta)

@app.route("/api/chat", methods=["POST"])
def api_chat():
    msg = (request.get_json() or {}).get("message", "").strip()
    if not msg:
        return jsonify({"response": "Please type or speak a medical question.", "intent": "", "confidence": 0})
    return jsonify(predict(msg))

@app.route("/api/models")
def api_models():
    """Return model accuracy comparison for the UI."""
    return jsonify(model_meta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
