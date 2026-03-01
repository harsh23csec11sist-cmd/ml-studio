# 🩺 MedBot — Medical AI Chatbot

> **Doctor-level AI medical assistant** built with Python, Flask, and NLP (TF-IDF + Cosine Similarity). Ask about diseases, medications, lab values, first aid, and more — no external API required.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) ![Flask](https://img.shields.io/badge/Flask-3.1-black?logo=flask) ![scikit-learn](https://img.shields.io/badge/scikit--learn-NLP-orange?logo=scikit-learn) ![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🦠 **40+ Medical Topics** — Diseases, conditions, symptoms covered in clinical detail
- 💊 **Medications** — Drug uses, dosages, side effects, contraindications
- 🩸 **Lab Values & Vitals** — Blood pressure, blood sugar, hemoglobin, cholesterol, SpO2, BMI
- 🚑 **First Aid & Emergencies** — CPR, Heimlich, snakebite, burns
- 🧠 **Mental Health** — Depression, anxiety, panic attacks with DSM-5 criteria
- 🥗 **Nutrition & Lifestyle** — Evidence-based dietary and exercise advice
- 💬 **Real-time Chat UI** — Typing animation, quick-question chips, AJAX messaging

---

## 🧠 How It Works

```
User Input
    │
    ▼
TF-IDF Vectorizer (char n-grams 2–4)
    │
    ▼
Cosine Similarity → Best matching intent
    │
    ▼
Structured Medical Response
```

No GPT, no API keys. Uses **scikit-learn TF-IDF** + **cosine similarity** on a curated medical knowledge base with 200+ training patterns.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/medical-ai-chatbot.git
cd medical-ai-chatbot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the chatbot model
python train.py

# 5. Run the app
python app.py
```

Open **http://localhost:5000** in your browser.

---

## 📁 Project Structure

```
medical-ai-chatbot/
├── app.py                  # Flask application (routes + inference)
├── train.py                # Model training script
├── knowledge_base.py       # Doctor-level medical knowledge base (40+ intents)
├── requirements.txt        # Python dependencies
├── Procfile                # Render/Heroku deployment
├── build.sh                # Build script (trains model on deploy)
├── templates/
│   ├── index.html          # Landing page
│   └── chat.html           # Chat interface
└── static/
    └── css/
        └── style.css       # Styling (dark theme, responsive)
```

---

## 🏥 Medical Topics Covered

| Category | Topics |
|----------|--------|
| 🦠 Diseases | Diabetes (T1/T2), Hypertension, Malaria, TB, COVID-19, Dengue, Typhoid, Pneumonia, Asthma |
| ❤️ Cardiology | Heart Attack (MI), Angina, Heart Failure, Coronary Artery Disease |
| 🩸 Hematology | Anemia (Iron-deficiency, B12, Folate), Hemoglobin values |
| 🦴 MSK | Osteoarthritis, Rheumatoid Arthritis, Gout, Back Pain |
| 🌸 Women's Health | PCOS, Menstrual health |
| 🧠 Mental Health | Depression (MDD), Anxiety, Panic Attacks (DSM-5 criteria) |
| 🦋 Endocrinology | Hypothyroidism, Hyperthyroidism, TSH levels |
| 💊 Pharmacology | Paracetamol, Ibuprofen, Metformin, Antibiotics, Aspirin |
| 🩸 Lab Values | Blood pressure, Blood sugar, HbA1c, Hemoglobin, Cholesterol, SpO2, BMI |
| 🚑 Emergency | Heart attack, Stroke, CPR, Choking, Snakebite, Burns |
| 🥗 Nutrition | Vitamins (D, C, B12), Minerals (Iron, Calcium), Omega-3 |

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, Flask 3.1 |
| ML / NLP | scikit-learn (TF-IDF, Cosine Similarity), NumPy |
| Model Persistence | joblib |
| Frontend | HTML5, Vanilla CSS, Vanilla JS (Fetch API) |
| Deployment | Render (free tier), Gunicorn |

---

## 🌐 Deploy on Render (Free)

1. Push to GitHub
2. Create new **Web Service** on [Render](https://render.com)
3. Settings:
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn app:app`
4. Deploy! 🚀

---

## ⚠️ Medical Disclaimer

> MedBot provides **general health information only**. It is **NOT** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified, licensed physician for any health concerns.

---

## 📝 License

MIT License — free to use, modify, and distribute.

---

*Built with ❤️ using Python, Flask & scikit-learn*
