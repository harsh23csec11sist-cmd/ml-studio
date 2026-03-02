"""
MedBot — Hybrid ML + LLM Medical AI Chatbot
============================================
Pipeline:
  Step 1 → TF-IDF + ML Classifier detects medical INTENT
  Step 2 → Groq Llama 3.3 70B generates natural doctor-like RESPONSE
            using detected intent + confidence as rich context

Routes:
  GET  /           → Landing page
  GET  /chat       → Chat interface
  POST /api/chat   → JSON: {"message": "...", "history": [...]}
                         → {"response": "...", "intent": "...", "confidence": 95.3, "model": "SVM"}
  GET  /api/models → Returns ML model accuracy + training stats
"""

import os, json, joblib
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app    = Flask(__name__)
BASE   = os.path.dirname(os.path.abspath(__file__))
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ── Load ML Models ─────────────────────────────────────────────────────────────
def load_model(name):
    return joblib.load(os.path.join(BASE, "models", name))

best_model    = load_model("best_model.pkl")
label_encoder = load_model("label_encoder.pkl")
knowledge     = load_model("knowledge.pkl")

with open(os.path.join(BASE, "models", "model_meta.json")) as f:
    model_meta = json.load(f)

CONFIDENCE_THRESHOLD = 0.25   # below this → LLM gets no ML hint


# ── ML Intent Detection ─────────────────────────────────────────────────────────
def detect_intent(user_input: str) -> dict:
    """
    Stage 1: Run TF-IDF + ML classifier to detect medical intent.
    Returns dict: {tag, confidence, top_responses}
    """
    text  = [user_input.lower().strip()]
    proba = best_model.predict_proba(text)[0]
    top_idx = int(proba.argmax())
    conf    = float(proba[top_idx])
    tag     = label_encoder.inverse_transform([top_idx])[0]

    # Get top-3 intents for richer context
    top3_idx = proba.argsort()[-3:][::-1]
    top3 = [(label_encoder.inverse_transform([i])[0], round(float(proba[i])*100, 1))
            for i in top3_idx]

    # Get knowledge base responses for the detected intent
    top_responses = knowledge["intent_map"].get(
        tag,
        knowledge["intent_map"].get(knowledge["fallback"], [])
    )

    return {
        "tag":           tag,
        "confidence":    round(conf * 100, 1),
        "top3":          top3,
        "top_responses": top_responses[:2],   # send top 2 KB answers as hints
        "model_used":    model_meta["best_model"],
    }


# ── LLM Doctor Response (Stage 2) ──────────────────────────────────────────────
SYSTEM_PROMPT_BASE = """You are Dr. MedBot, a highly experienced, board-certified physician with expertise \
across general medicine, cardiology, endocrinology, neurology, psychiatry, pharmacology, and emergency care.

Your personality:
- Warm, empathetic and reassuring — like a trusted family doctor
- You speak in clear, simple language patients can understand
- You use medical terminology when helpful, always explaining it
- You ask thoughtful follow-up questions to understand the patient better
- You give practical, actionable advice

Your response style:
- Conversational and natural — NOT just bullet point lists every time
- Mix well-structured paragraphs with key points when needed
- For serious symptoms (chest pain, stroke, difficulty breathing) ALWAYS urge emergency care immediately
- Mention when a specific test, medication, or specialist referral is warranted

IMPORTANT: Always end with a brief reminder that your advice is informational and the patient \
should see a licensed physician for proper diagnosis and treatment."""


def build_system_prompt(ml_result: dict) -> str:
    """Inject ML-detected intent as context into the LLM system prompt."""
    prompt = SYSTEM_PROMPT_BASE

    if ml_result["confidence"] >= CONFIDENCE_THRESHOLD * 100:
        intent_tag   = ml_result["tag"].replace("_", " ").title()
        confidence   = ml_result["confidence"]
        kb_hints     = "\n".join(f"- {r}" for r in ml_result["top_responses"])

        prompt += f"""

--- INTERNAL ML CONTEXT (do NOT mention to patient) ---
The patient's message has been classified by your internal ML diagnostic system:
  • Detected Medical Intent : {intent_tag}
  • ML Classifier Confidence: {confidence}%
  • Model Used              : {ml_result['model_used']} (TF-IDF features)
  • Knowledge Base Hints    :
{kb_hints}

Use this context to give a more targeted, medically accurate response. \
If the intent doesn't match the patient's actual message, trust the message itself."""

    return prompt


# ── Groq LLM Call ──────────────────────────────────────────────────────────────
def get_llm_response(user_message: str, history: list, ml_result: dict) -> str:
    """Stage 2: Send to Groq Llama 3.3 70B with enriched doctor system prompt."""
    system_prompt = build_system_prompt(ml_result)

    messages = [{"role": "system", "content": system_prompt}]

    # Include last 10 turns of history for context
    for turn in history[-10:]:
        if turn.get("role") in ("user", "assistant") and turn.get("content"):
            messages.append({"role": turn["role"], "content": turn["content"]})

    messages.append({"role": "user", "content": user_message})

    completion = client.chat.completions.create(
        model       = "llama-3.3-70b-versatile",
        messages    = messages,
        temperature = 0.7,
        max_tokens  = 1024,
        top_p       = 0.9,
    )
    return completion.choices[0].message.content


# ── Routes ──────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", meta=model_meta)


@app.route("/chat")
def chat():
    return render_template("chat.html", meta=model_meta)


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data        = request.get_json() or {}
    user_message = data.get("message", "").strip()
    history      = data.get("history", [])

    if not user_message:
        return jsonify({"response": "Please ask me a medical question — I'm here to help! 🩺",
                        "intent": "", "confidence": 0})
    try:
        # ── Stage 1: ML Intent Detection ────────────────────
        ml_result = detect_intent(user_message)

        # ── Stage 2: LLM Natural Response ───────────────────
        response_text = get_llm_response(user_message, history, ml_result)

        return jsonify({
            "response":   response_text,
            "intent":     ml_result["tag"].replace("_", " ").title(),
            "confidence": ml_result["confidence"],
            "ml_model":   ml_result["model_used"],
            "top3":       ml_result["top3"],
        })

    except Exception as e:
        return jsonify({"response": f"⚠️ Something went wrong: {str(e)}. Please try again.",
                        "intent": "", "confidence": 0})


@app.route("/api/models")
def api_models():
    """Return ML model accuracy report."""
    return jsonify(model_meta)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"✅ MedBot Hybrid ML+LLM starting on port {port}")
    print(f"   ML Model: {model_meta['best_model']} | Accuracy: {max(model_meta['accuracy'].values()):.1%}")
    print(f"   LLM: Groq Llama 3.3 70B")
    app.run(debug=False, host="0.0.0.0", port=port)
