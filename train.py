"""
MedBot Training Script — ML Algorithm Pipeline
Trains & evaluates 3 ML classifiers:
  1. LinearSVC (Support Vector Machine)  — Best for text
  2. MultinomialNB (Naive Bayes)          — Fast, probabilistic
  3. Logistic Regression                  — Interpretable

Best model (by accuracy) is saved as the production model.
Run: python train.py
"""
import os, json, joblib, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from knowledge_base import INTENTS

os.makedirs("models", exist_ok=True)

# ── Build corpus ──────────────────────────────────────────────────────────────
corpus, labels = [], []
for intent in INTENTS:
    for pattern in intent["patterns"]:
        corpus.append(pattern.lower())
        labels.append(intent["tag"])

le = LabelEncoder()
y  = le.fit_transform(labels)

print(f"\n📊 Dataset: {len(corpus)} samples | {len(le.classes_)} classes\n")

# ── Shared TF-IDF Vectorizer ──────────────────────────────────────────────────
tfidf = TfidfVectorizer(
    analyzer      = "char_wb",   # character n-grams — typo tolerant
    ngram_range   = (2, 4),
    max_features  = 12000,
    sublinear_tf  = True,
    strip_accents = "unicode",
)


# ── Train & Evaluate each model ───────────────────────────────────────────────
results = {}

# 1. Support Vector Machine (LinearSVC)
print("Training LinearSVC (SVM)...")
svm_pipe = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,4), max_features=12000, sublinear_tf=True)),
    ("clf",   CalibratedClassifierCV(LinearSVC(C=1.0, max_iter=2000), cv=3)),
])
svm_scores = cross_val_score(svm_pipe, corpus, y, cv=5, scoring="accuracy")
svm_pipe.fit(corpus, y)
results["SVM (LinearSVC)"] = svm_scores.mean()
print(f"  ✅ SVM Accuracy: {svm_scores.mean():.3f} ± {svm_scores.std():.3f}")

# 2. Naive Bayes (MultinomialNB)
print("Training Naive Bayes (MultinomialNB)...")
nb_pipe = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,4), max_features=12000, sublinear_tf=True, min_df=1)),
    ("clf",   MultinomialNB(alpha=0.1)),
])
nb_scores = cross_val_score(nb_pipe, corpus, y, cv=5, scoring="accuracy")
nb_pipe.fit(corpus, y)
results["Naive Bayes (MultinomialNB)"] = nb_scores.mean()
print(f"  ✅ NB Accuracy:  {nb_scores.mean():.3f} ± {nb_scores.std():.3f}")

# 3. Logistic Regression
print("Training Logistic Regression...")
lr_pipe = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,4), max_features=12000, sublinear_tf=True)),
    ("clf",   LogisticRegression(C=5.0, max_iter=1000, solver="lbfgs")),
])
lr_scores = cross_val_score(lr_pipe, corpus, y, cv=5, scoring="accuracy")
lr_pipe.fit(corpus, y)
results["Logistic Regression"] = lr_scores.mean()
print(f"  ✅ LR Accuracy:  {lr_scores.mean():.3f} ± {lr_scores.std():.3f}")

# ── Pick best model ───────────────────────────────────────────────────────────
best_name = max(results, key=results.get)
best_pipe = {"SVM (LinearSVC)": svm_pipe, "Naive Bayes (MultinomialNB)": nb_pipe, "Logistic Regression": lr_pipe}[best_name]

print(f"\n🏆 Best model: {best_name} ({results[best_name]:.3f} accuracy)")

# ── Save models ───────────────────────────────────────────────────────────────
intent_map = {i["tag"]: i["responses"] for i in INTENTS}
fallback_tag = "fallback"

joblib.dump(best_pipe,  "models/best_model.pkl")
joblib.dump(le,         "models/label_encoder.pkl")
joblib.dump(svm_pipe,   "models/svm_model.pkl")
joblib.dump(nb_pipe,    "models/nb_model.pkl")
joblib.dump(lr_pipe,    "models/lr_model.pkl")

# Save metadata
meta = {
    "best_model": best_name,
    "accuracy": {k: round(v, 4) for k, v in results.items()},
    "num_intents": len(le.classes_),
    "num_samples": len(corpus),
    "classes": le.classes_.tolist(),
}
with open("models/model_meta.json", "w") as f:
    json.dump(meta, f, indent=2)

joblib.dump({"intent_map": intent_map, "fallback": fallback_tag}, "models/knowledge.pkl")

print("\n✅ Saved:")
print("   models/best_model.pkl      ← Production model")
print("   models/svm_model.pkl       ← SVM (LinearSVC)")
print("   models/nb_model.pkl        ← Naive Bayes")
print("   models/lr_model.pkl        ← Logistic Regression")
print("   models/label_encoder.pkl   ← Class labels")
print("   models/knowledge.pkl       ← Medical responses")
print("   models/model_meta.json     ← Accuracy report")
print("\n🎉 Training complete!")
