"""
Medical AI Chatbot — Doctor-Level Knowledge Base
Covers: diseases, symptoms, drugs, vitals, labs, emergencies, mental health, nutrition
"""

INTENTS = [
    # ── Greetings ────────────────────────────────────────────────────
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "good morning", "good evening", "namaste", "hii", "howdy"],
        "responses": [
            "Hello! I'm MedBot 🩺 — your AI Medical Assistant. Ask me about symptoms, diseases, medications, lab values, or first aid.\n\n⚠️ I provide general medical information only. Always consult a licensed physician for personal advice.",
        ],
    },
    {"tag": "thanks", "patterns": ["thanks", "thank you", "thx", "great", "helpful", "awesome"],
     "responses": ["Happy to help! Stay healthy 🌿. Always consult a doctor for personal medical care."]},
    {"tag": "who_are_you", "patterns": ["who are you", "are you a doctor", "what are you", "can you diagnose me"],
     "responses": ["I am MedBot 🤖 — an AI trained on medical knowledge based on clinical guidelines. I am NOT a substitute for a real physician. Always seek professional care for diagnosis and treatment."]},

    # ── EMERGENCY ────────────────────────────────────────────────────
    {
        "tag": "emergency",
        "patterns": ["emergency", "call ambulance", "not breathing", "unconscious", "stroke", "heart attack now", "overdose", "poisoning", "severe bleeding", "someone collapsed", "dying"],
        "responses": [
            "🚨 CALL 112 (India) / 911 (USA) IMMEDIATELY!\n\nWhile waiting:\n• Keep calm and still\n• If unconscious but breathing → recovery position\n• If not breathing → Begin CPR (30 compressions : 2 breaths)\n• Do NOT give food/water\n• Stay on the line with emergency services"
        ],
    },

    # ── VITAL SIGNS ──────────────────────────────────────────────────
    {
        "tag": "blood_pressure",
        "patterns": ["normal blood pressure", "bp range", "hypertension values", "high blood pressure numbers", "what is normal bp", "blood pressure 140 90", "blood pressure 120 80", "hypotension"],
        "responses": [
            "🩺 Blood Pressure Reference (mmHg):\n\n✅ Normal: <120/80\n⚠️ Elevated: 120–129/<80\n🔴 Stage 1 HTN: 130–139 / 80–89\n🔴 Stage 2 HTN: ≥140/90\n🚨 Hypertensive Crisis: >180/120 → Emergency\n💙 Hypotension: <90/60\n\n💡 Confirm hypertension with multiple readings on different days. Single reading is not enough."
        ],
    },
    {
        "tag": "blood_sugar",
        "patterns": ["normal blood sugar", "fasting glucose", "blood glucose level", "sugar level", "hba1c", "postprandial glucose", "random blood sugar", "diabetes values"],
        "responses": [
            "🩸 Blood Glucose Reference:\n\nFasting:\n✅ Normal: 70–100 mg/dL\n⚠️ Prediabetes: 100–125 mg/dL\n🔴 Diabetes: ≥126 mg/dL\n\n2-hr Post-meal:\n✅ Normal: <140 mg/dL\n⚠️ Prediabetes: 140–199 mg/dL\n🔴 Diabetes: ≥200 mg/dL\n\nHbA1c:\n✅ Normal: <5.7%\n⚠️ Prediabetes: 5.7–6.4%\n🔴 Diabetes: ≥6.5%"
        ],
    },
    {
        "tag": "temperature",
        "patterns": ["normal body temperature", "fever temperature", "what temperature is fever", "body temp", "high temperature", "hypothermia"],
        "responses": [
            "🌡️ Body Temperature:\n\n✅ Normal: 36.1–37.2°C (97–99°F)\n🟡 Low-grade fever: 37.3–38°C\n🔴 Fever: ≥38°C (100.4°F)\n🔴 High fever: ≥39.5°C (103°F)\n🚨 Hyperpyrexia: >41°C (106°F) — Emergency\n💙 Hypothermia: <35°C (95°F)\n\n💊 Adult treatment: Paracetamol 500–1000mg every 4–6h. Stay hydrated."
        ],
    },
    {
        "tag": "spo2",
        "patterns": ["normal oxygen level", "spo2", "oxygen saturation", "pulse oximeter", "low oxygen", "oxygen 95", "oxygen 90"],
        "responses": [
            "🫁 SpO2 (Oxygen Saturation):\n\n✅ Normal: 95–100%\n⚠️ Mild hypoxemia: 91–94% → Monitor closely\n🔴 Moderate: 86–90% → Seek medical care\n🚨 Severe: ≤85% → Emergency\n\n⚠️ COVID-19: SpO2 <94% → immediate evaluation needed\n💡 COPD patients may have baseline 88–92% — ask their doctor for target range."
        ],
    },
    {
        "tag": "heart_rate",
        "patterns": ["normal heart rate", "pulse rate", "resting heart rate", "bradycardia", "tachycardia", "bpm normal", "high heart rate"],
        "responses": [
            "❤️ Heart Rate Reference:\n\n✅ Normal (adults): 60–100 bpm\n✅ Athletes: 40–60 bpm (normal for them)\n⚠️ Bradycardia: <60 bpm\n⚠️ Tachycardia: >100 bpm\n🚨 Seek help if >150 bpm at rest with dizziness/chest pain/fainting"
        ],
    },
    {
        "tag": "bmi",
        "patterns": ["bmi normal", "body mass index", "overweight", "obese bmi", "underweight bmi", "healthy weight range", "bmi chart"],
        "responses": [
            "⚖️ BMI Chart:\n\n• Underweight: <18.5\n• Normal: 18.5–24.9\n• Overweight: 25–29.9\n• Obese Class I: 30–34.9\n• Obese Class II: 35–39.9\n• Severe Obesity: ≥40\n\nFormula: Weight(kg) ÷ Height(m)²\n\n⚠️ BMI doesn't account for muscle mass or body fat distribution."
        ],
    },

    # ── LAB VALUES ───────────────────────────────────────────────────
    {
        "tag": "hemoglobin",
        "patterns": ["normal hemoglobin", "low hemoglobin", "anemia hemoglobin", "hb level", "hemoglobin range", "cbc normal"],
        "responses": [
            "🩸 Hemoglobin (Hb) Reference:\n\n• Adult Men: 13.5–17.5 g/dL\n• Adult Women: 12–15.5 g/dL\n• Pregnant: ≥11 g/dL\n• Children: 11–16 g/dL (age-dependent)\n\nAnemia severity:\n• Mild: 10–12 g/dL\n• Moderate: 7–9.9 g/dL\n• Severe: <7 g/dL → may need transfusion"
        ],
    },
    {
        "tag": "cholesterol",
        "patterns": ["normal cholesterol", "ldl hdl", "cholesterol levels", "triglycerides", "lipid profile", "high cholesterol"],
        "responses": [
            "💉 Lipid Panel Reference:\n\n• Total Cholesterol: <200 mg/dL ✅\n• LDL (bad): <100 mg/dL optimal; <70 for high-risk\n• HDL (good): >40 (men), >50 (women); >60 = protective\n• Triglycerides: <150 mg/dL ✅\n\n🥗 Reduce saturated fats, increase omega-3 & fiber\n💊 Statins (Atorvastatin) if lifestyle insufficient"
        ],
    },

    # ── DISEASES ─────────────────────────────────────────────────────
    {
        "tag": "diabetes",
        "patterns": ["diabetes symptoms", "what is diabetes", "type 1 diabetes", "type 2 diabetes", "signs of diabetes", "diabetes treatment", "diabetic diet", "insulin resistance", "diabetes causes", "diabetes management"],
        "responses": [
            "🩺 Diabetes Mellitus:\n\n📌 Type 1: Autoimmune — requires insulin. Onset: childhood/young adults.\n📌 Type 2: Insulin resistance. 90% of cases. Managed with diet, exercise, medications.\n\n⚠️ Classic Symptoms (3 Ps):\n• Polyuria (frequent urination)\n• Polydipsia (excessive thirst)\n• Polyphagia (excessive hunger)\n+ Weight loss, blurred vision, slow-healing wounds, tingling/numbness\n\n💊 Medications:\n• Metformin (first-line T2DM)\n• SGLT2 inhibitors (empagliflozin)\n• GLP-1 agonists (semaglutide)\n• Insulin (T1DM + severe T2DM)\n\n🎯 Targets: HbA1c <7%, FBS <130, BP <130/80\n🥗 Diet: Low GI foods, high fiber, avoid sugary drinks"
        ],
    },
    {
        "tag": "hypertension",
        "patterns": ["hypertension symptoms", "high bp symptoms", "hypertension treatment", "how to lower blood pressure", "antihypertensive", "hypertension causes", "hypertension diet", "bp treatment"],
        "responses": [
            "🩺 Hypertension (High Blood Pressure):\n\n📌 'Silent Killer' — often NO symptoms until severe\n\n⚠️ Severe symptoms: morning headache, blurred vision, nosebleeds, chest pain\n\n🔑 Causes: Obesity, high salt, sedentary lifestyle, stress, genetics, kidney disease, sleep apnea\n\n💊 Drug Classes:\n• ACE inhibitors: Enalapril, Lisinopril\n• ARBs: Losartan, Valsartan\n• CCBs: Amlodipine (first-line)\n• Diuretics: Hydrochlorothiazide\n• Beta-blockers: Metoprolol, Atenolol\n\n🥗 DASH Diet: Salt <2g/day, high potassium (bananas, spinach), no smoking/alcohol, exercise ≥150 min/week"
        ],
    },
    {
        "tag": "fever",
        "patterns": ["how to treat fever", "fever treatment", "fever in adults", "fever remedies", "paracetamol fever", "fever management", "high fever", "fever causes", "fever in children", "when to see doctor fever"],
        "responses": [
            "🌡️ Fever Management:\n\n💊 Treatment:\n• Paracetamol (Acetaminophen): 500–1000mg every 4–6h (adults). Max 4g/day.\n• Ibuprofen: 400mg every 6–8h WITH food.\n• ❌ NO Aspirin for children (Reye's syndrome risk)\n\n🏠 Home Care:\n• Rest + oral hydration (ORS, coconut water, water)\n• Lukewarm sponge bath (NOT ice/cold)\n• Light clothing — don't over-bundle\n\n🚨 See Doctor urgently if:\n• Fever >39.5°C lasting >3 days\n• Infant <3 months with ANY fever\n• Fever + rash, stiff neck, confusion, severe headache"
        ],
    },
    {
        "tag": "malaria",
        "patterns": ["malaria symptoms", "what is malaria", "malaria treatment", "malaria causes", "plasmodium", "malaria diagnosis", "antimalarial", "falciparum malaria", "malaria prevention"],
        "responses": [
            "🦟 Malaria:\n\n📌 Caused by Plasmodium spp. (P. falciparum = most deadly). Spread by female Anopheles mosquito.\n\n⚠️ Symptoms (7–30 days after bite):\n• Cyclical fever & chills (every 48–72h)\n• Drenching sweats, headache, body aches\n• Nausea, vomiting, fatigue\n• Jaundice + anemia (severe cases)\n\n🔬 Diagnosis: Peripheral blood smear (gold standard), RDT, PCR\n\n💊 Treatment:\n• Uncomplicated: Artemether-Lumefantrine (Coartem)\n• Severe P. falciparum: IV Artesunate\n• Prophylaxis: Doxycycline, Atovaquone-Proguanil\n\n🛡️ Prevention: mosquito nets, DEET repellent, eliminate standing water"
        ],
    },
    {
        "tag": "tuberculosis",
        "patterns": ["tb symptoms", "tuberculosis", "what is tb", "tb treatment", "latent tb", "tb bacteria", "dots treatment", "mycobacterium", "tb diagnosis"],
        "responses": [
            "🫁 Tuberculosis (TB):\n\n📌 Caused by Mycobacterium tuberculosis. Airborne transmission.\n\n⚠️ Active TB Symptoms:\n• Persistent cough >3 weeks (may have blood)\n• Low-grade evening fever + night sweats\n• Weight loss, fatigue\n• Chest pain\n\n🔬 Diagnosis: Chest X-ray, Sputum AFB smear/GeneXpert, IGRA, Mantoux test\n\n💊 DOTS Therapy:\n• Intensive (2 months): HRZE (Isoniazid + Rifampicin + Pyrazinamide + Ethambutol)\n• Continuation (4 months): HR\n• Total: 6 months minimum\n\n⚠️ Rifampicin → orange urine/tears (harmless)\n⚠️ Isoniazid → supplement Pyridoxine (B6) to prevent neuropathy"
        ],
    },
    {
        "tag": "covid19",
        "patterns": ["covid symptoms", "coronavirus", "covid treatment", "omicron", "covid 19", "covid positive", "covid isolation", "long covid"],
        "responses": [
            "🦠 COVID-19:\n\n⚠️ Common Symptoms:\n• Fever, dry cough, fatigue\n• Loss of taste/smell (anosmia)\n• Sore throat, headache, body aches\n• Shortness of breath (severe cases)\n\n🏠 Mild Home Care:\n• Isolate ≥5 days\n• Paracetamol for fever/pain\n• Monitor SpO2 (seek help if <94%)\n• Prone positioning helps oxygenation\n• Stay hydrated\n\n🚨 Hospitalize if: SpO2 <90%, severe breathlessness, chest pain, confusion\n\n💊 Treatments (doctor-supervised): Paxlovid (Nirmatrelvir-Ritonavir), Remdesivir, Corticosteroids (severe)\n🛡️ Prevention: Vaccination + masks + hand hygiene"
        ],
    },
    {
        "tag": "dengue",
        "patterns": ["dengue symptoms", "dengue fever", "dengue treatment", "dengue platelet", "aedes mosquito", "breakbone fever", "dengue warning signs", "dengue diagnosis"],
        "responses": [
            "🦟 Dengue Fever:\n\n📌 Viral; spread by Aedes aegypti (daytime biting).\n\n⚠️ Classic Symptoms (4–10 days post-bite):\n• Sudden high fever (39–40°C)\n• Severe headache, retro-orbital pain (behind eyes)\n• Severe joint/muscle pain ('Breakbone fever')\n• Skin rash, nausea/vomiting, mild bleeding\n\n🚨 Dengue Warning Signs (Severe — Emergency):\n• Persistent abdominal pain\n• Vomiting blood / black stools\n• Platelet <20,000 — hemorrhage risk\n• Rapid breathing, lethargy\n\n💊 Treatment (NO specific antiviral):\n• Paracetamol ONLY for fever (❌ NOT aspirin/ibuprofen → bleeding risk)\n• IV fluids if severe\n• Daily platelet monitoring\n\n🛡️ Prevention: eliminate stagnant water, mosquito repellent"
        ],
    },
    {
        "tag": "typhoid",
        "patterns": ["typhoid symptoms", "enteric fever", "typhoid treatment", "typhoid causes", "salmonella", "typhoid diet", "typhoid diagnosis", "widal test"],
        "responses": [
            "🦠 Typhoid Fever (Enteric Fever):\n\n📌 Caused by Salmonella typhi. Spread via contaminated food/water.\n\n⚠️ Symptoms (step-ladder fever):\n• Gradually rising fever (39–40°C) for 1–3 weeks\n• Headache, abdominal pain, relative bradycardia\n• Rose spots on trunk\n• Constipation early → 'Pea-soup' diarrhea late\n\n🔬 Diagnosis: Blood culture (gold standard — week 1), Widal test (less specific)\n\n💊 Treatment:\n• Azithromycin (oral, uncomplicated)\n• Ceftriaxone IV (severe/hospitalized)\n\n🍚 Diet: Bland, easily digestible foods. Stay very hydrated.\n🛡️ Prevention: TCV vaccine, safe water, hand hygiene"
        ],
    },
    {
        "tag": "pneumonia",
        "patterns": ["pneumonia symptoms", "lung infection", "pneumonia treatment", "bacterial pneumonia", "viral pneumonia", "pneumonia causes", "pneumonia diagnosis"],
        "responses": [
            "🫁 Pneumonia:\n\n📌 Infection of lung alveoli. Most common cause: Streptococcus pneumoniae.\n\n⚠️ Symptoms:\n• Fever, chills, night sweats\n• Productive cough (yellow/green/rust sputum)\n• Pleuritic chest pain (worse on breathing)\n• Shortness of breath, rapid breathing\n\n🔬 Diagnosis: Chest X-ray (gold standard), CBC (elevated WBC), sputum culture\n\n💊 Treatment:\n• Community-acquired (outpatient): Amoxicillin or Azithromycin\n• Hospital: IV Ceftriaxone + Azithromycin\n• Viral: Supportive (antivirals for influenza)\n\n🚨 Hospitalize if: SpO2 <92%, RR >30/min, confusion, hypotension"
        ],
    },
    {
        "tag": "asthma",
        "patterns": ["asthma symptoms", "asthma attack", "asthma treatment", "wheezing", "bronchial asthma", "inhaler", "asthma triggers", "shortness of breath asthma"],
        "responses": [
            "🫁 Asthma:\n\n📌 Chronic reversible airway inflammation.\n\n⚠️ Symptoms:\n• Wheezing, shortness of breath (especially at night/exercise)\n• Chest tightness, dry cough\n\n🔑 Triggers: Dust mites, pollen, cold air, smoke, exercise, NSAIDs\n\n💊 Treatment:\n• Reliever (SABA): Salbutamol inhaler (acute attacks)\n• Controller (ICS): Budesonide/Beclomethasone (daily)\n• Combination: Formoterol + Budesonide (moderate-severe)\n• Montelukast (leukotriene antagonist)\n\n🚨 Acute Attack: 2–4 puffs salbutamol, sit upright, call emergency if no improvement in 15 min"
        ],
    },
    {
        "tag": "heart_disease",
        "patterns": ["heart attack symptoms", "myocardial infarction", "angina", "heart failure symptoms", "coronary artery disease", "signs of heart attack", "cardiac symptoms", "chest pain heart"],
        "responses": [
            "❤️ Heart Attack (MI) Warning Signs — 🚨 EMERGENCY:\n\n• Crushing chest pressure/pain → radiates to left arm, jaw, back\n• Shortness of breath, cold sweat, nausea\n• Lightheadedness\n• Women: may have fatigue, jaw pain, nausea (atypical)\n\n→ Call 112 immediately. Chew Aspirin 300–325mg (if not allergic) while awaiting help.\n\n📌 Stable Angina: exertional chest pain relieved by rest or Nitroglycerin.\n📌 Heart Failure: ankle swelling, breathlessness lying flat, reduced exercise tolerance.\n\n💊 Key Drugs: Aspirin, Statins (Atorvastatin), Beta-blockers (Metoprolol), ACE inhibitors, Diuretics (Furosemide)"
        ],
    },
    {
        "tag": "anemia",
        "patterns": ["anemia symptoms", "iron deficiency anemia", "low hemoglobin symptoms", "anemia treatment", "pale skin anemia", "anemia diet", "b12 deficiency", "folate deficiency"],
        "responses": [
            "🩸 Anemia:\n\n⚠️ Symptoms:\n• Fatigue, weakness, shortness of breath on exertion\n• Pale skin/conjunctiva/nails\n• Dizziness, cold hands/feet, rapid heartbeat\n• Pica (craving ice/clay) → iron deficiency\n\n📊 Types & Treatment:\n• Iron-deficiency (most common): Ferrous sulfate + eat iron-rich foods (lentils, spinach, red meat) with Vitamin C\n• B12 deficiency: IM Cyanocobalamin injections or oral B12\n• Folate deficiency: Folic acid 5mg daily\n• Hemolytic/Aplastic: specialist management\n\n🚨 Hb <7 g/dL or symptomatic → may need blood transfusion"
        ],
    },
    {
        "tag": "uti",
        "patterns": ["uti symptoms", "urinary tract infection", "burning urination", "frequent urination", "bladder infection", "kidney infection", "urine infection", "uti treatment"],
        "responses": [
            "🦠 Urinary Tract Infection (UTI):\n\n📌 Most common: E. coli. More common in women.\n\n⚠️ Symptoms:\n• Burning/painful urination (dysuria)\n• Urgency and frequency\n• Cloudy/foul-smelling urine, hematuria\n• Lower abdominal discomfort\n\n🚨 Upper UTI (Pyelonephritis):\n• Fever, chills, flank pain (back under ribs), nausea/vomiting\n→ Needs IV antibiotics\n\n💊 Treatment:\n• Uncomplicated: Nitrofurantoin 5–7 days, or TMP-SMX 3 days\n• Alternative: Ciprofloxacin 500mg BD × 3 days\n• Pyelonephritis: Ciprofloxacin/Ceftriaxone 10–14 days\n\n💧 Drink plenty of water. UTI in men/children/pregnancy needs thorough evaluation."
        ],
    },
    {
        "tag": "thyroid",
        "patterns": ["thyroid symptoms", "hypothyroidism", "hyperthyroidism", "tsh level", "thyroid treatment", "goiter", "graves disease", "hashimoto", "thyroid disorder"],
        "responses": [
            "🦋 Thyroid Disorders:\n\nTSH Normal: 0.4–4.0 mIU/L\n\n📌 Hypothyroidism (Underactive — TSH HIGH):\n• Weight gain, cold intolerance, constipation\n• Fatigue, depression, dry skin, hair loss, bradycardia\n• Cause: Hashimoto's thyroiditis, iodine deficiency\n• Treatment: Levothyroxine (T4) — lifelong\n\n📌 Hyperthyroidism (Overactive — TSH LOW):\n• Weight loss despite appetite↑, heat intolerance, sweating\n• Palpitations, tremors, anxiety, insomnia, exophthalmos\n• Cause: Graves' disease, toxic nodule\n• Treatment: Carbimazole/PTU, radioactive iodine, thyroidectomy\n\n🔬 Tests: TSH + Free T4 + Free T3 + Anti-TPO antibodies"
        ],
    },
    {
        "tag": "arthritis",
        "patterns": ["arthritis symptoms", "joint pain", "rheumatoid arthritis", "osteoarthritis", "gout", "morning stiffness", "knee pain", "joint swelling"],
        "responses": [
            "🦴 Arthritis:\n\n📌 Osteoarthritis (OA): degenerative, worse with use, elderly\n📌 Rheumatoid Arthritis (RA): autoimmune, symmetrical, morning stiffness >1 hour\n📌 Gout: uric acid crystals, sudden severe pain (big toe/ankle)\n\n💊 Treatment:\n• OA: Paracetamol, NSAIDs (Ibuprofen), physiotherapy\n• RA (DMARDs): Methotrexate (first-line), Hydroxychloroquine, Biologics (TNF-α inhibitors)\n• Gout (acute): Colchicine or NSAIDs; Long-term: Allopurinol (lowers uric acid)\n\n🥗 Gout diet: avoid red meat, shellfish, beer, sugary drinks"
        ],
    },
    {
        "tag": "pcos",
        "patterns": ["pcos symptoms", "polycystic ovary", "irregular periods pcos", "pcos treatment", "pcos diet", "pcos causes", "acne pcos", "fertility pcos"],
        "responses": [
            "🌸 PCOS (Polycystic Ovarian Syndrome):\n\n📌 Most common endocrine disorder in women of reproductive age.\n\nDiagnosis (Rotterdam Criteria — 2 of 3):\n1. Irregular/absent periods\n2. Hyperandrogenism (acne, hirsutism, hair loss)\n3. Polycystic ovaries on ultrasound\n\n+ Insulin resistance, weight gain, infertility, acanthosis nigricans\n\n💊 Treatment:\n• OCP (regulates cycle, reduces androgens)\n• Metformin (insulin resistance + cycle regulation)\n• Clomiphene/Letrozole (ovulation induction)\n• Spironolactone (hirsutism/acne)\n\n🥗 Even 5–10% weight loss dramatically improves symptoms\n🔬 Tests: LH/FSH ratio, free testosterone, pelvic ultrasound"
        ],
    },

    # ── MENTAL HEALTH ─────────────────────────────────────────────────
    {
        "tag": "depression",
        "patterns": ["depression symptoms", "i feel depressed", "clinical depression", "major depressive disorder", "antidepressants", "feeling hopeless", "no motivation", "persistent sadness", "depression treatment"],
        "responses": [
            "💙 Depression (MDD):\n\n⚠️ Symptoms (≥5 for ≥2 weeks; must include #1 or #2):\n1. Depressed mood most of the day\n2. Loss of interest/pleasure (anhedonia)\n3. Weight/appetite change\n4. Sleep disturbance (insomnia or hypersomnia)\n5. Fatigue\n6. Worthlessness/guilt\n7. Poor concentration\n8. Psychomotor changes\n9. Suicidal ideation\n\n💊 Treatment:\n• SSRIs (first-line): Sertraline, Fluoxetine, Escitalopram (takes 4–6 weeks)\n• SNRIs: Venlafaxine, Duloxetine\n• CBT (Cognitive Behavioral Therapy) equally effective for mild-moderate\n• Combination (drug + therapy) = best outcomes\n\n🚨 Suicidal thoughts → iCall: 9152987821 (India) or call 112"
        ],
    },
    {
        "tag": "anxiety",
        "patterns": ["anxiety symptoms", "panic attack", "generalized anxiety", "i feel anxious", "anxiety treatment", "social anxiety", "anxiety disorder", "breathing exercises anxiety"],
        "responses": [
            "🧠 Anxiety Disorders:\n\n📌 GAD: excessive worry ≥6 months about multiple things\n📌 Panic Attack: sudden intense fear, peaks in ~10 min\n📌 Social Anxiety: fear of social situations\n\n⚠️ Panic Attack Symptoms:\n• Racing heart, chest pain, shortness of breath\n• Sweating, trembling, dizziness, feeling of doom\n\n💊 Treatment:\n• SSRIs/SNRIs (first-line, long-term)\n• Buspirone (non-addictive for GAD)\n• Benzodiazepines (short-term only — dependence risk)\n• CBT (highly effective for all anxiety disorders)\n\n🧘 Immediate relief: 4-7-8 breathing (inhale 4s, hold 7s, exhale 8s)\n5-4-3-2-1 grounding (5 things you see, 4 touch, 3 hear, 2 smell, 1 taste)"
        ],
    },

    # ── MEDICATIONS ───────────────────────────────────────────────────
    {
        "tag": "paracetamol",
        "patterns": ["paracetamol dosage", "paracetamol uses", "acetaminophen", "crocin", "dolo 650", "paracetamol overdose", "paracetamol side effects"],
        "responses": [
            "💊 Paracetamol (Acetaminophen / Crocin / Dolo 650):\n\n📌 Uses: Fever, mild-moderate pain (headache, toothache, body ache)\n\nDosage:\n• Adults: 500–1000mg every 4–6h as needed\n• Maximum: 4000mg (4g) per day\n• Children: 10–15mg/kg every 4–6h\n\n✅ Generally very safe at recommended doses\n\n🚨 DANGER:\n• Overdose → acute liver failure (even 6–8g can be fatal)\n• + Alcohol → increases liver toxicity\n• Hidden in cold/flu medications — check labels to avoid double-dosing"
        ],
    },
    {
        "tag": "ibuprofen",
        "patterns": ["ibuprofen dosage", "ibuprofen uses", "brufen", "nsaid", "anti-inflammatory drug", "ibuprofen side effects"],
        "responses": [
            "💊 Ibuprofen (Brufen / Advil):\n\n📌 Class: NSAID\n📌 Uses: Pain, fever, inflammation\n\nDosage:\n• Adults: 400–600mg every 6–8h WITH food\n• Max: 2400mg/day\n\n⚠️ Side Effects: GI irritation, ulcers, GI bleeding, fluid retention\n\n🚫 Avoid in:\n• Peptic ulcer, kidney/liver disease, heart failure\n• Dengue (bleeding risk)\n• Pregnancy (3rd trimester)\n• Children <6 months"
        ],
    },
    {
        "tag": "metformin",
        "patterns": ["metformin uses", "metformin dosage", "metformin side effects", "glucophage", "biguanide", "diabetes medication metformin"],
        "responses": [
            "💊 Metformin (Glucophage):\n\n📌 First-line drug for Type 2 Diabetes. Also used in PCOS.\n\nDosage:\n• Start: 500mg once daily with meals\n• Increase to 500–1000mg twice daily\n• Maximum: 2550mg/day\n\n✅ Benefits: No hypoglycemia alone, weight neutral, cardioprotective, cheap\n\n⚠️ Side Effects: Nausea, diarrhea (usually improves over time; use XR form)\n\n🚨 Lactic acidosis (rare): risk in kidney failure, alcohol excess\n🚫 Hold 48h before IV contrast procedures"
        ],
    },
    {
        "tag": "antibiotics",
        "patterns": ["what are antibiotics", "antibiotic uses", "amoxicillin", "azithromycin", "ciprofloxacin", "antibiotic resistance", "when to take antibiotics", "broad spectrum antibiotic"],
        "responses": [
            "💊 Antibiotics:\n\n⚠️ ONLY work on bacteria — NOT viruses (cold, flu, COVID, dengue)\n\nCommon Antibiotics:\n• Amoxicillin: respiratory, ENT, UTI\n• Azithromycin (Z-Pack): atypical pneumonia, STIs\n• Ciprofloxacin: UTI, GI infections, typhoid\n• Doxycycline: malaria prophylaxis, acne, chest infections\n• Metronidazole: anaerobic/GI infections, H. pylori\n• Ceftriaxone: serious hospital infections (IV)\n\n🚨 Key Rules:\n• Complete the FULL course (even if feeling better)\n• Never share or self-medicate with antibiotics\n• Antibiotic Resistance is a critical global health crisis"
        ],
    },
    {
        "tag": "aspirin",
        "patterns": ["aspirin uses", "aspirin dosage", "aspirin heart attack", "baby aspirin", "aspirin side effects", "when to take aspirin", "acetylsalicylic acid"],
        "responses": [
            "💊 Aspirin (Acetylsalicylic Acid):\n\nUses:\n• Pain/fever: 325–650mg every 4–6h\n• Antiplatelet (heart protection): 75–100mg/day\n• Heart attack: Chew 300–325mg immediately\n\n✅ Prevents clots → reduces MI/stroke risk\n\n⚠️ Side Effects: GI bleeding, tinnitus at high doses\n\n🚫 NEVER give to children/teens with viral illness (Reye's syndrome)\n🚫 Avoid in: dengue, peptic ulcer, 3rd trimester pregnancy"
        ],
    },

    # ── SYMPTOMS ──────────────────────────────────────────────────────
    {
        "tag": "chest_pain",
        "patterns": ["chest pain causes", "left side chest pain", "chest tightness", "stabbing chest pain", "chest pain when breathing"],
        "responses": [
            "🚨 Chest Pain — Red Flags (Call 112 immediately):\n• Crushing/pressure pain radiating to arm, jaw, back\n• Sweating, nausea, shortness of breath → cardiac emergency\n\nOther Causes:\n• GERD/acid reflux: burning, worse after meals, relieved by antacids\n• Costochondritis: tender on pressing sternal border, benign\n• Pleuritis/pneumonia: sharp, worse on breathing\n• Pulmonary embolism: sudden onset, with leg pain/swelling\n• Anxiety/panic attack: can mimic cardiac pain\n\n⚠️ Any new unexplained chest pain → always get ECG and medical evaluation"
        ],
    },
    {
        "tag": "headache",
        "patterns": ["headache types", "migraine", "tension headache", "cluster headache", "headache treatment", "severe headache", "headache remedies", "migraine treatment"],
        "responses": [
            "🧠 Headache Types:\n\n📌 Tension (most common): bilateral band-like pressure, mild-moderate\n→ Paracetamol, Ibuprofen, rest, stress management\n\n📌 Migraine: unilateral pulsating, moderate-severe + nausea, photo/phonophobia\n→ Triptans (Sumatriptan) acute; Topiramate/Amitriptyline prevention\n\n📌 Cluster: excruciating unilateral periorbital pain + tearing; clusters over weeks\n→ 100% O2, Sumatriptan injection\n\n🚨 Emergency Red Flags:\n• 'Thunderclap' headache (worst of life) → subarachnoid hemorrhage\n• Fever + stiff neck + headache → meningitis\n• New headache in elderly or after trauma"
        ],
    },
    {
        "tag": "back_pain",
        "patterns": ["back pain", "lower back pain", "disc herniation", "backache", "sciatica", "lumbar pain", "back pain treatment", "spine pain"],
        "responses": [
            "🦴 Back Pain:\n\nCauses:\n• Muscle strain (most common) — poor posture, lifting\n• Disc herniation (PIVD): pain radiating to leg (sciatica)\n• Ankylosing spondylitis: young men, morning stiffness\n• Spondylosis (elderly)\n\n💊 Treatment:\n• Paracetamol or NSAIDs for pain\n• Muscle relaxants if spasm (Cyclobenzaprine)\n• Physiotherapy: core strengthening (most effective long-term)\n• Hot/cold compresses\n\n🚨 Red Flags (Urgent):\n• Bowel/bladder dysfunction → cauda equina (surgical emergency)\n• Saddle anesthesia, progressive leg weakness\n• Fever + back pain → vertebral osteomyelitis\n• Weight loss + elderly → malignancy"
        ],
    },

    # ── FIRST AID ─────────────────────────────────────────────────────
    {
        "tag": "first_aid",
        "patterns": ["cpr steps", "how to do cpr", "first aid", "choking", "heimlich maneuver", "burns first aid", "wound first aid", "snake bite first aid", "someone fainted"],
        "responses": [
            "🚑 Basic First Aid:\n\n❤️ CPR (Adult):\n1. Call 112\n2. 30 chest compressions (center of chest, 2 inches deep, 100–120/min)\n3. 2 rescue breaths (head-tilt, chin-lift)\n4. Repeat 30:2 until help arrives\n\n🍗 Choking (Heimlich):\n• Adult: 5 back blows + 5 abdominal upward thrusts\n• Infant: 5 back blows + 5 chest thrusts\n\n🔥 Burns:\n• Cool running water 10–20 min (NOT ice)\n• Cover with non-fluffy clean material\n• Don't burst blisters\n\n🐍 Snakebite:\n• Keep calm and still\n• Immobilize bitten limb at heart level\n• No incision, suction, tourniquet\n• Get antivenom ASAP"
        ],
    },

    # ── NUTRITION ─────────────────────────────────────────────────────
    {
        "tag": "nutrition",
        "patterns": ["healthy diet", "vitamin d deficiency", "vitamin c", "iron rich foods", "calcium", "omega 3", "balanced diet", "nutrition tips", "vitamins minerals"],
        "responses": [
            "🥗 Nutrition Essentials:\n\n• Vitamin D: bone & immunity. Sources: sunlight, fatty fish. Supplement: 1000–4000 IU/day\n• Vitamin C: antioxidant. Sources: citrus, bell peppers.\n• Iron: hemoglobin. Sources: lentils, spinach, red meat. Take with Vitamin C; avoid with tea/coffee.\n• Calcium: bones. Sources: dairy, sesame, ragi. Needs Vitamin D for absorption.\n• B12: nerve function (deficient in vegetarians/vegans). Supplement: 500mcg/day\n• Omega-3: heart & brain. Sources: salmon, walnuts, flaxseed.\n\n🏆 Best evidence-based diets:\n• Mediterranean: best for cardiovascular & longevity\n• DASH: best for hypertension"
        ],
    },

    # ── FALLBACK ──────────────────────────────────────────────────────
    {
        "tag": "fallback",
        "patterns": [],
        "responses": [
            "I'm not sure about that. You can ask me about:\n• 🦠 Diseases (diabetes, TB, malaria, COVID-19, dengue, typhoid...)\n• 💊 Medications (paracetamol, metformin, antibiotics...)\n• 🩸 Lab values (blood pressure, blood sugar, cholesterol...)\n• 🚑 First aid & emergencies\n• 🧠 Mental health (depression, anxiety...)\n• 🥗 Nutrition & lifestyle",
        ],
    },
]
