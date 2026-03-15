import streamlit as st
import random

# ==========================================
# PART 1: THE DATASET (PASTE QUESTIONS HERE)
# ==========================================

def get_all_questions():
    return {
        # --- PASTE BATCHES 1, 2, AND 3 BELOW THIS LINE ---
        "Preparatory & Airway": [
            {"q": "Which structure is the dividing line between the upper and lower airway?", "options": ["Pharynx", "Larynx", "Trachea", "Carina"], "correct": "Larynx", "rationale": "The larynx (vocal cords) is the transition point. Above is upper, below is lower."},
            {"q": "The phrenic nerve controls the diaphragm. Where does it exit the spine?", "options": ["C1-C2", "C3-C5", "T1-T4", "L1-L2"], "correct": "C3-C5", "rationale": "REMEMBER: 'C3, 4, and 5 keep the diaphragm alive.'"},
            {"q": "What is the leaf-shaped cartilage that prevents aspiration?", "options": ["Cricoid", "Epiglottis", "Carina", "Thyroid"], "correct": "Epiglottis", "rationale": "It covers the glottic opening during swallowing to protect the trachea."},
            {"q": "Where does gas exchange specifically occur?", "options": ["Bronchi", "Alveoli", "Trachea", "Pleura"], "correct": "Alveoli", "rationale": "Diffusion of O2 and CO2 happens at the alveolar-capillary membrane."},
            {"q": "The primary drive to breathe is based on levels of:", "options": ["Oxygen", "Carbon Dioxide", "pH", "Glucose"], "correct": "Carbon Dioxide", "rationale": "The brain monitors CO2 levels in the CSF (Hypercarbic Drive)."},
            {"q": "The 'Hypoxic Drive' is found in late-stage:", "options": ["Asthma", "COPD", "Pneumonia", "CHF"], "correct": "COPD", "rationale": "These patients rely on low oxygen levels to trigger breathing."},
            {"q": "What happens to chest pressure during inhalation?", "options": ["Becomes Positive", "Becomes Negative", "Stays Neutral", "Doubles"], "correct": "Becomes Negative", "rationale": "The diaphragm drops, creating a vacuum (negative pressure) to pull air in."},
            {"q": "Max suction time for an adult:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "15 sec", "rationale": "To prevent hypoxia."},
            {"q": "Adult ventilation rate (BVM):", "options": ["Every 3 sec", "Every 5-6 sec", "Every 10 sec", "Every 1 sec"], "correct": "Every 5-6 sec", "rationale": "10-12 breaths per minute."},
            {"q": "Trauma patient airway maneuver?", "options": ["Head-tilt chin-lift", "Jaw-thrust", "Neck lift", "Trendelenburg"], "correct": "Jaw-thrust", "rationale": "Protects the cervical spine."},
            {"q": "What is 'Dead Space'?", "options": ["Air not reaching alveoli", "Air left after exhalation", "Air in a pneumothorax", "BVM volume"], "correct": "Air not reaching alveoli", "rationale": "Air in the trachea/bronchi that does not participate in gas exchange."},
            {"q": "Minute Volume is calculated as:", "options": ["TV + RR", "TV x RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Tidal Volume x Respiratory Rate = Minute Volume."},
            {"q": "A high-pitched whistling sound on inhalation is:", "options": ["Wheezing", "Stridor", "Rales", "Rhonchi"], "correct": "Stridor", "rationale": "Indicates upper airway obstruction (e.g., croup, foreign body)."},
            {"q": "Wheezing typically indicates:", "options": ["Upper airway obstruction", "Lower airway constriction", "Fluid in lungs", "Tongue blockage"], "correct": "Lower airway constriction", "rationale": "Air whistling through narrowed bronchioles (Asthma/COPD)."},
            {"q": "Gurgling sounds indicate:", "options": ["Fluid in the airway", "Tongue obstruction", "Swelling", "Normal breathing"], "correct": "Fluid in the airway", "rationale": "Immediate need for suctioning."},
            {"q": "Snoring sounds usually indicate:", "options": ["Fluid", "Tongue obstruction", "Bronchospasm", "Infection"], "correct": "Tongue obstruction", "rationale": "The tongue has fallen back against the pharynx."},
            {"q": "Cyanosis (blue skin) is a late sign of:", "options": ["High CO2", "Hypoxia", "Low blood sugar", "Shock"], "correct": "Hypoxia", "rationale": "Significant lack of oxygen in the blood."},
            {"q": "Max suction time for a child:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "10 sec", "rationale": "Children have less oxygen reserve."},
            {"q": "Max suction time for an infant:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "5 sec", "rationale": "Infants desaturate extremely fast."},
            {"q": "How do you size an OPA?", "options": ["Corner of mouth to earlobe", "Tip of nose to earlobe", "Corner of mouth to angle of jaw", "Nose to chin"], "correct": "Corner of mouth to angle of jaw", "rationale": "Ensures the device sits properly to hold the tongue."},
            {"q": "Contraindication for an OPA:", "options": ["Gag reflex", "No teeth", "Skull fracture", "Fluid in airway"], "correct": "Gag reflex", "rationale": "It will cause vomiting and aspiration."},
            {"q": "Contraindication for an NPA:", "options": ["Gag reflex", "Basilar skull fracture", "Seizure", "Stroke"], "correct": "Basilar skull fracture", "rationale": "Risk of pushing the tube into the brain cavity."},
            {"q": "Suction should be applied:", "options": ["On insertion", "On withdrawal", "Continuously", "Intermittently"], "correct": "On withdrawal", "rationale": "Insert without suction, apply suction while pulling out in a circular motion."},
            {"q": "FiO2 of Room Air is approx:", "options": ["16%", "21%", "50%", "100%"], "correct": "21%", "rationale": "The atmosphere is ~21% oxygen."},
            {"q": "Nasal Cannula flow range:", "options": ["1-6 LPM", "6-10 LPM", "10-15 LPM", "15-25 LPM"], "correct": "1-6 LPM", "rationale": "Delivers 24-44% oxygen concentrations."},
            {"q": "Non-Rebreather (NRB) flow rate:", "options": ["6-10 LPM", "10-15 LPM", "1-6 LPM", "25 LPM"], "correct": "10-15 LPM", "rationale": "Must be high enough to keep the reservoir bag inflated."},
            {"q": "Venturi Mask is best for:", "options": ["Trauma", "COPD", "Cardiac Arrest", "Shock"], "correct": "COPD", "rationale": "It delivers a precise, fixed concentration of oxygen."},
            {"q": "BVM with reservoir delivers approx:", "options": ["21%", "50%", "80%", "Nearly 100%"], "correct": "Nearly 100%", "rationale": "High flow O2 + reservoir bag = max oxygenation."},
            {"q": "Child/Infant ventilation rate (BVM):", "options": ["Every 3-5 sec", "Every 6-8 sec", "Every 10 sec", "Every 2 sec"], "correct": "Every 3-5 sec", "rationale": "12-20 breaths per minute."},
            {"q": "Gastric distension is caused by:", "options": ["Ventilating too fast/hard", "Using an OPA", "Suctioning", "Using a cannula"], "correct": "Ventilating too fast/hard", "rationale": "Air enters the stomach instead of lungs."},
            {"q": "Best indicator of effective ventilation:", "options": ["Chest rise", "SpO2 increases", "Skin color improves", "Normal HR"], "correct": "Chest rise", "rationale": "Visible chest rise is the immediate sign of success."},
            {"q": "Sellick Maneuver (Cricoid Pressure) prevents:", "options": ["Gastric distension", "Vomiting", "Hypoxia", "Aspiration"], "correct": "Gastric distension", "rationale": "Compresses the esophagus against the spine."},
            {"q": "CPAP stands for:", "options": ["Continuous Positive Airway Pressure", "Constant Pulmonary Airway Pressure", "Cardiopulmonary Airway Pressure", "None of these"], "correct": "Continuous Positive Airway Pressure", "rationale": "Maintains pressure to keep alveoli open."},
            {"q": "Primary indication for CPAP:", "options": ["Apnea", "Pulmonary Edema/CHF", "Pneumothorax", "Trauma"], "correct": "Pulmonary Edema/CHF", "rationale": "Pushes fluid out of alveoli to improve gas exchange."},
            {"q": "Strict contraindication for CPAP:", "options": ["Hypotension (Low BP)", "Hypertension", "Tachypnea", "Low O2"], "correct": "Hypotension (Low BP)", "rationale": "CPAP increases chest pressure, which drops BP further."},
            {"q": "If air escapes the mouth during stoma ventilation:", "options": ["Seal mouth and nose", "Press harder", "Suction stoma", "Stop"], "correct": "Seal mouth and nose", "rationale": "You must create a closed circuit to ensure air reaches the lungs."},
            {"q": "DOPE: 'D' stands for:", "options": ["Dislodgement", "Death", "Distension", "Drugs"], "correct": "Dislodgement", "rationale": "Tube has moved out of position."},
            {"q": "DOPE: 'O' stands for:", "options": ["Oxygen", "Obstruction", "Overdose", "Output"], "correct": "Obstruction", "rationale": "Mucus or secretions are blocking the tube."},
            {"q": "DOPE: 'P' stands for:", "options": ["Pneumonia", "Pneumothorax", "Pulse", "Pain"], "correct": "Pneumothorax", "rationale": "Collapsed lung detected by unequal breath sounds."},
            {"q": "DOPE: 'E' stands for:", "options": ["Edema", "Embolism", "Equipment", "Energy"], "correct": "Equipment", "rationale": "Check oxygen source and tubing connections."},
            {"q": "The 'E-C' clamp technique is used for:", "options": ["Holding a mask seal", "Checking a pulse", "Sizing an OPA", "Holding a nebulizer"], "correct": "Holding a mask seal", "rationale": "Thumbs/Index (C) on mask, other fingers (E) on jaw."},
            {"q": "What is the primary function of the surfactant in the lungs?", "options": ["Reduce surface tension in the alveoli", "Facilitate the exchange of gases", "Lubricate the pleural membranes", "Prevent infection"], "correct": "Reduce surface tension in the alveoli", "rationale": "Surfactant prevents the alveoli from collapsing during exhalation."},
            {"q": "In a patient with suspected epiglottitis, what should be avoided?", "options": ["Inspecting the throat with a tongue depressor", "Administering oxygen", "Keeping the patient upright", "Providing fluids"], "correct": "Inspecting the throat with a tongue depressor", "rationale": "Irritating the epiglottis can cause total airway spasm and closure."},
            {"q": "A patient with 'Pleuritic' chest pain. What does this mean?", "options": ["Pain that worsens with deep breathing", "Pain that radiates to the left arm", "Pain that is constant and crushing", "Pain relieved by eating"], "correct": "Pain that worsens with deep breathing", "rationale": "Inflamed pleural linings rub together during inspiration."},
            {"q": "What is the function of the 'Carina'?", "options": ["Point where the trachea bifurcates into bronchi", "Cartilage that protects vocal cords", "Valve between pharynx and esophagus", "Space between lungs"], "correct": "Point where the trachea bifurcates into bronchi", "rationale": "The last point of the trachea before it splits."},
            {"q": "What is 'Atelectasis'?", "options": ["Collapse of the alveoli", "Fluid in the pleural space", "Infection of bronchioles", "Spasm of vocal cords"], "correct": "Collapse of the alveoli", "rationale": "Prevents gas exchange in the affected area of the lung."},
            {"q": "What is the normal EtCO2 range?", "options": ["35-45 mmHg", "25-35 mmHg", "45-55 mmHg", "80-100 mmHg"], "correct": "35-45 mmHg", "rationale": "Represents the normal balance of CO2 production and ventilation."},
            {"q": "Which respiratory pattern has increasing/decreasing breaths followed by apnea?", "options": ["Cheyne-Stokes", "Kussmaul", "Biot's", "Ataxic"], "correct": "Cheyne-Stokes", "rationale": "Often associated with heart failure or central nervous system injuries."}
            # (Note: Use these to fill the remaining slots for your 88-question Preparatory module)
           
        ],
        "Pharmacology": [
            {"q": "What are the three key responsibilities of an EMT regarding medication safety?", "options": ["Diagnosis, prescription, and follow-up", "Cross-check, correct dose/route, and monitoring", "Billing, driving, and inventory", "Intubation and sedation"], "correct": "Cross-check, correct dose/route, and monitoring", "rationale": "Standard safety responsibility."},
            {"q": "What is the adult dose for Aspirin for cardiac chest pain?", "options": ["81 mg", "162 mg", "324 mg", "500 mg"], "correct": "324 mg", "rationale": "Four 81mg chewable tablets."},
            {"q": "Nitro is contraindicated if Systolic BP is below:", "options": ["120", "110", "100", "90"], "correct": "100", "rationale": "Systolic must be > 100 per most protocols."},
            {"q": "Mechanism of Narcan:", "options": ["Sedative", "Competitive opioid antagonist", "Beta-blocker", "Benzodiazepine"], "correct": "Competitive opioid antagonist", "rationale": "Competes for receptors to restore breathing."},
            {"q": "Suffix for Beta-Blockers:", "options": ["-pril", "-sartan", "-olol", "-statin"], "correct": "-olol", "rationale": "e.g., Metoprolol."},
            {"q": "Epinephrine causes:", "options": ["Vasodilation/Bronchoconstriction", "Vasoconstriction/Bronchodilation", "Lower heart rate", "Decreased BP"], "correct": "Vasoconstriction/Bronchodilation", "rationale": "Epi reverses anaphylaxis by opening airways and raising blood pressure."},
            {"q": "Oral Glucose is used for:", "options": ["Hyperglycemia", "Hypoglycemia", "Chest Pain", "Asthma"], "correct": "Hypoglycemia", "rationale": "It raises blood sugar in conscious patients with an intact gag reflex."},
            {"q": "Nitroglycerin is a:", "options": ["Vasoconstrictor", "Vasodilator", "Bronchodilator", "Sedative"], "correct": "Vasodilator", "rationale": "It dilates coronary arteries to improve blood flow to the heart muscle."},
            {"q": "Zofran is used to treat:", "options": ["Pain", "Nausea/Vomiting", "Seizures", "Allergic reactions"], "correct": "Nausea/Vomiting", "rationale": "It is an anti-emetic often used in EMS for motion sickness or nausea."},
            {"q": "What is the primary effect of a Beta-2 agonist like Albuterol?", "options": ["Bronchodilation", "Vasoconstriction", "Lower HR", "Mucus production"], "correct": "Bronchodilation", "rationale": "Beta-2 receptors relax bronchial smooth muscle."},
            {"q": "Common side effect of Albuterol:", "options": ["Tachycardia and tremors", "Bradycardia and lethargy", "Hypotension", "Abdominal pain"], "correct": "Tachycardia and tremors", "rationale": "Albuterol is a sympathomimetic and stimulates Beta-1 (heart) slightly too."},
            {"q": "Standard adult dose for Epinephrine 1:1,000 for anaphylaxis (IM):", "options": ["0.3 mg", "0.15 mg", "1.0 mg", "3.0 mg"], "correct": "0.3 mg", "rationale": "Adult standard is 0.3 mg; 0.15 mg is the pediatric dose."},
            {"q": "How does magnesium sulfate work in asthma treatment?", "options": ["Bronchial smooth muscle relaxant", "Reduces inflammation", "Inhibits histamine", "Increases cardiac output"], "correct": "Bronchial smooth muscle relaxant", "rationale": "Magnesium relaxes the muscles of the bronchi to improve airflow."},
            {"q": "What is the purpose of administering steroids in asthma?", "options": ["To reduce inflammation", "To relieve bronchospasm", "To increase inflammation", "To prevent allergic reactions"], "correct": "To reduce inflammation", "rationale": "Steroids are a long-term 'controller' medication that reduces airway swelling."},
            {"q": "Which drug class is typically first-line for COPD management?", "options": ["Bronchodilators", "Anticholinergics", "Corticosteroids", "Antihistamines"], "correct": "Bronchodilators", "rationale": "They provide immediate relief by relaxing airway muscles."},
            {"q": "Why is caution used with oxygen in Paraquat poisoning?", "options": ["It worsens lung fibrosis", "It causes cardiac arrest", "It triggers seizures", "It leads to acidosis"], "correct": "It worsens lung fibrosis", "rationale": "Oxygen accelerates the oxidative damage caused by the chemical Paraquat."},
            {"q": "Pulse Oximetry may give a falsely HIGH reading in:", "options": ["Carbon monoxide poisoning", "Hypothermia", "Nail polish", "Anemia"], "correct": "Carbon monoxide poisoning", "rationale": "The oximeter cannot distinguish between oxygen-saturated and CO-saturated hemoglobin."},
            {"q": "Target SpO2 for a patient with COPD is usually:", "options": ["88-92%", "94-99%", "100%", "90-100%"], "correct": "88-92%", "rationale": "Higher levels can suppress the hypoxic drive to breathe in chronic COPD patients."},
            {"q": "Which medication is an example of an 'Anticholinergic' used in respiratory distress?", "options": ["Albuterol", "Atrovent (Ipratropium)", "Epinephrine", "Solu-Medrol"], "correct": "Atrovent (Ipratropium)", "rationale": "Atrovent blocks acetylcholine to prevent bronchoconstriction; often paired with Albuterol (DuoNeb)."},
            {"q": "What is the suffix typically found in ACE Inhibitor medications?", "options": ["-olol", "-pril", "-sartan", "-statin"], "correct": "-pril", "rationale": "Examples include Lisinopril and Enalapril. They are used to treat hypertension."},
            {"q": "What is the suffix typically found in Beta-Blocker medications?", "options": ["-olol", "-pril", "-dipine", "-caine"], "correct": "-olol", "rationale": "Examples include Metoprolol and Atenolol. They lower heart rate and blood pressure."},
            {"q": "Which suffix is associated with ARBs (Angiotensin II Receptor Blockers)?", "options": ["-statin", "-sartan", "-prazole", "-afil"], "correct": "-sartan", "rationale": "Examples include Losartan and Valsartan."},
            {"q": "Medications ending in '-statin' (e.g., Atorvastatin) are used for:", "options": ["High Blood Pressure", "High Cholesterol", "Diabetes", "Blood Clots"], "correct": "High Cholesterol", "rationale": "Statins lower LDL cholesterol and reduce risk of cardiovascular disease."},
            {"q": "A patient taking Warfarin (Coumadin) or Clopidogrel (Plavix) is on:", "options": ["Anti-platelets/Anticoagulants", "Antihypertensives", "Anticonvulsants", "Antidotes"], "correct": "Anti-platelets/Anticoagulants", "rationale": "These are 'blood thinners' that increase the risk of significant bleeding in trauma."},
            {"q": "Which of the following is a Calcium Channel Blocker?", "options": ["Amlodipine", "Lisinopril", "Metoprolol", "Furosemide"], "correct": "Amlodipine", "rationale": "Suffix '-dipine' usually indicates a Calcium Channel Blocker used for BP."},
            {"q": "What is the primary concern when a patient takes 'ED medications' (e.g., Viagra) and Nitroglycerin?", "options": ["Severe Hypertension", "Severe Hypotension", "Seizures", "Tachycardia"], "correct": "Severe Hypotension", "rationale": "Both are potent vasodilators; combined, they can cause a fatal drop in blood pressure."},
            {"q": "Metformin is a common medication for which condition?", "options": ["Type 1 Diabetes", "Type 2 Diabetes", "Asthma", "Heart Failure"], "correct": "Type 2 Diabetes", "rationale": "It is an oral hypoglycemic agent that decreases glucose production in the liver."},
            {"q": "What does a 'Sympathomimetic' drug do?", "options": ["Mimics the Sympathetic Nervous System", "Blocks the Fight-or-Flight response", "Slows the heart rate", "Constricts the pupils"], "correct": "Mimics the Sympathetic Nervous System", "rationale": "It 'mimics' the 'fight-or-flight' response (e.g., Epinephrine)."},
            {"q": "Which medication is an 'Adsorption' agent used for ingested poisons?", "options": ["Syrup of Ipecac", "Activated Charcoal", "Oral Glucose", "Narcan"], "correct": "Activated Charcoal", "rationale": "Adsorption means the toxin binds to the surface of the charcoal."},
            {"q": "What is the 'Generic' name for the trade name Benadryl?", "options": ["Diphenhydramine", "Hydroxyzine", "Epinephrine", "Loratadine"], "correct": "Diphenhydramine", "rationale": "Benadryl is the trade/brand name; Diphenhydramine is the generic name."},
            {"q": "Which of these is the correct adult dose for an Epi-Pen?", "options": ["0.3 mg", "0.15 mg", "3.0 mg", "1.0 mg"], "correct": "0.3 mg", "rationale": "0.3 mg is the standard adult dose; 0.15 mg is the 'Junior' or Pediatric dose."},
            {"q": "What is the route of administration for Nitroglycerin spray/tablet?", "options": ["Oral", "Sublingual", "Buccal", "Subcutaneous"], "correct": "Sublingual", "rationale": "Placed under the tongue for rapid absorption through the mucous membranes."},
            {"q": "A 'Side Effect' is defined as:", "options": ["A life-threatening reaction", "Any effect of a drug other than the desired one", "An allergic reaction", "A reason not to give a drug"], "correct": "Any effect of a drug other than the desired one", "rationale": "Side effects can be predictable and harmless, or unpleasant (like dry mouth)."},
            {"q": "What is a 'Contraindication'?", "options": ["A reason to give a drug", "A reason NOT to give a drug", "The desired effect", "How the drug is packaged"], "correct": "A reason NOT to give a drug", "rationale": "Situations where the drug would be harmful to the patient."},
            {"q": "Which drug is used specifically to increase the heart rate in symptomatic bradycardia?", "options": ["Atropine", "Adenosine", "Amiodarone", "Atenolol"], "correct": "Atropine", "rationale": "Atropine is a parasympatholytic that speeds up the heart."},
            {"q": "The medication used to stabilize the heart in 'Hyperkalemia' is:", "options": ["Calcium Chloride", "Sodium Bicarbonate", "Albuterol", "Insulin"], "correct": "Calcium Chloride", "rationale": "Stabilizes the cardiac cell membrane during high potassium levels."},
            {"q": "What is the 'Trade Name' of a drug?", "options": ["The name given by the manufacturer", "The chemical structure", "The name in the USP", "The government name"], "correct": "The name given by the manufacturer", "rationale": "Also known as the Brand Name (e.g., Tylenol)."},
            {"q": "How many 'mg' are in one 'gram'?", "options": ["10 mg", "100 mg", "1000 mg", "10,000 mg"], "correct": "1000 mg", "rationale": "Standard metric conversion: 1g = 1000mg."},
            {"q": "Which of the '6 Rights' involves checking the expiration date?", "options": ["Right Patient", "Right Medication", "Right Dose", "Right Time"], "correct": "Right Medication", "rationale": "Checking the label for name and expiration is part of identifying the Right Medication."},
            {"q": "If you are 'Assisting' a patient with their own Nitro, you must ensure:", "options": ["The medication is prescribed to them", "The BP is > 100", "They haven't taken ED meds", "All of the above"], "correct": "All of the above", "rationale": "Assisting requires the same safety checks as administering."},
            {"q": "What is the primary risk of using a MDI (Metered Dose Inhaler) incorrectly?", "options": ["Medication ends up in the back of the throat/stomach", "Immediate overdose", "The inhaler might explode", "None"], "correct": "Medication ends up in the back of the throat/stomach", "rationale": "Proper timing and breathing are required for the drug to reach the lower airways."},
            {"q": "A 'Suspension' medication (like Activated Charcoal) must be:", "options": ["Shaken before use", "Injected", "Inhaled", "Filtered"], "correct": "Shaken before use", "rationale": "Suspensions contain particles that settle at the bottom over time."},
            {"q": "Which medication is an 'Antipyretic'?", "options": ["Ibuprofen", "Albuterol", "Nitroglycerin", "Narcan"], "correct": "Ibuprofen", "rationale": "Antipyretic means 'fever-reducer.'"},
            {"q": "Furosemide (Lasix) is a 'Diuretic.' What is its purpose?", "options": ["Increase BP", "Remove excess fluid from the body", "Treat infection", "Stop bleeding"], "correct": "Remove excess fluid from the body", "rationale": "Commonly used in CHF to reduce pulmonary edema."},
            {"q": "Which medication is typically found in a DuoDote kit?", "options": ["Atropine and 2-PAM", "Epinephrine and Narcan", "Nitro and Aspirin", "Glucose and Charcoal"], "correct": "Atropine and 2-PAM", "rationale": "Used for nerve agent or organophosphate poisoning."},
            {"q": "When administering medication, the 'Cross-Check' involves:", "options": ["Having your partner verify the drug/dose", "Checking the map", "Checking the patient's ID", "Checking the bill"], "correct": "Having your partner verify the drug/dose", "rationale": "Reduces medical errors through a second set of eyes."},
            {"q": "Which of these is a potential 'Parenteral' route?", "options": ["Intramuscular (IM)", "Sublingual (SL)", "Oral (PO)", "Rectal (PR)"], "correct": "Intramuscular (IM)", "rationale": "Parenteral refers to routes that bypass the GI tract (usually injections/inhalations)."},
            {"q": "What does 'Tachyphylaxis' refer to?", "options": ["Rapidly decreasing response to a drug", "A fast heart rate", "Drug-induced seizure", "An allergic reaction"], "correct": "Rapidly decreasing response to a drug", "rationale": "Often seen with repeated doses of certain medications over a short period."},
            {"q": "A drug that 'potentiates' another drug:", "options": ["Decreases its effect", "Increases its effect", "Has no effect", "Neutralizes it"], "correct": "Increases its effect", "rationale": "Potentiation means one drug makes the other more powerful."},
            {"q": "Which organ is primarily responsible for the 'Metabolism' of drugs?", "options": ["Kidneys", "Liver", "Lungs", "Heart"], "correct": "Liver", "rationale": "The liver breaks down chemicals and drugs (first-pass metabolism)."},
            {"q": "Which organ is primarily responsible for the 'Excretion' of drugs?", "options": ["Kidneys", "Liver", "Skin", "Spleen"], "correct": "Kidneys", "rationale": "The kidneys filter drugs out of the blood into urine."},
            {"q": "What is the 'Therapeutic Index'?", "options": ["The price of a drug", "The margin between effectiveness and toxicity", "The list of side effects", "The time it takes to work"], "correct": "The margin between effectiveness and toxicity", "rationale": "A narrow index means a small difference between a helpful dose and a lethal one."},
            {"q": "Which of the following is a common 'Anti-emetic'?", "options": ["Ondansetron (Zofran)", "Lisinopril", "Metoprolol", "Albuterol"], "correct": "Ondansetron (Zofran)", "rationale": "Anti-emetics prevent or treat nausea and vomiting."},
            {"q": "Glucagon is administered when:", "options": ["The patient is hypoglycemic and you can't get an IV", "The patient is hyperglycemic", "The patient has chest pain", "The patient is in cardiac arrest"], "correct": "The patient is hypoglycemic and you can't get an IV", "rationale": "Glucagon triggers the liver to release stored glucose into the blood."},
            {"q": "Which medication is an 'Alpha-1' blocker used for BP or Prostate issues?", "options": ["Tamsulosin (Flomax)", "Albuterol", "Aspirin", "Epinephrine"], "correct": "Tamsulosin (Flomax)", "rationale": "Blocks Alpha-1 receptors to relax smooth muscle."},
            {"q": "What is the difference between an Agonist and an Antagonist?", "options": ["Agonists trigger a response; Antagonists block a response", "Agonists block; Antagonists trigger", "There is no difference", "Agonists are for kids; Antagonists are for adults"], "correct": "Agonists trigger a response; Antagonists block a response", "rationale": "Albuterol is a Beta-agonist; Propranolol is a Beta-antagonist (blocker)."},
            {"q": "What is the standard 'Six Rights' documentation protocol?", "options": ["Note the drug, dose, route, time, and patient response", "Just write 'Meds given'", "Tell the nurse at the hospital but don't write it", "Only document if it goes wrong"], "correct": "Note the drug, dose, route, time, and patient response", "rationale": "Accurate documentation is the 6th Right and ensures continuity of care."},
            {"q": "A patient with a 'Statin' medication in their history likely has:", "options": ["Hyperlipidemia", "Asthma", "Diabetes", "Seizures"], "correct": "Hyperlipidemia", "rationale": "Statins treat high lipid (fat/cholesterol) levels."},
            {"q": "A patient with 'Warfarin' in their history likely has a history of:", "options": ["Atrial Fibrillation or DVT", "Diabetes", "Asthma", "Allergies"], "correct": "Atrial Fibrillation or DVT", "rationale": "Warfarin prevents blood clots in high-risk patients."},
            {"q": "What is the route of administration for an Epi-Pen?", "options": ["Intramuscular", "Subcutaneous", "Intravenous", "Oral"], "correct": "Intramuscular", "rationale": "Injected into the lateral thigh muscle."},
            {"q": "What is the primary side effect of Nitroglycerin?", "options": ["Headache", "High BP", "Constipation", "Hives"], "correct": "Headache", "rationale": "Dilation of vessels in the brain often causes a throbbing headache."},
            {"q": "How many doses of Nitroglycerin can an EMT assist with for one episode?", "options": ["1", "3", "5", "Unlimited"], "correct": "3", "rationale": "Standard protocol allows up to 3 doses (5 mins apart) if BP remains stable."},
            {"q": "What is the dose of Narcan (Naloxone) via the IN (Intranasal) route?", "options": ["2-4 mg", "0.1 mg", "10 mg", "0.5 mg"], "correct": "2-4 mg", "rationale": "Standard pre-filled nasal sprays are usually 4mg."},
            {"q": "What is the concentration of Epinephrine used for IM injection in anaphylaxis?", "options": ["1:1,000", "1:10,000", "1:50", "1:100"], "correct": "1:1,000", "rationale": "1:1,000 is for IM; 1:10,000 is for IV/Cardiac arrest."},
            {"q": "Which medication is an 'Anti-cholinergic' used to treat organophosphate poisoning?", "options": ["Atropine", "Narcan", "Albuterol", "Aspirin"], "correct": "Atropine", "rationale": "Blocks the overstimulation caused by the poison."},
            {"q": "What is the mechanism of action for Activated Charcoal?", "options": ["Chemical neutralization", "Adsorption", "Absorption", "Osmosis"], "correct": "Adsorption", "rationale": "Binding particles to its surface."},

            # NOTE: Include all 71 questions from your Pharmacology bank here.
        ],
        "Trauma Review": [
            {"q": "What is the hallmark of decompensated shock?", "options": ["Mild anxiety", "Tachycardia", "Hypotension", "Cool skin"], "correct": "Hypotension", "rationale": "Once blood pressure drops, the body can no longer compensate."},
            {"q": "Beck's Triad (Cardiac Tamponade) consists of:", "options": ["HTN, Bradycardia, JVD", "Hypotension, JVD, muffled heart sounds", "Tachycardia, Hypotension, Clear lungs", "JVD, Hypotension, Wheezing"], "correct": "Hypotension, JVD, muffled heart sounds", "rationale": "These indicate the heart is being compressed by fluid in the pericardial sac."},
            {"q": "Cushing’s Triad (Increased ICP) consists of:", "options": ["Hypotension, Tachycardia, Tachypnea", "Hypertension, Bradycardia, irregular respirations", "Hypotension, Bradycardia, JVD", "Tachycardia, Muffled heart sounds"], "correct": "Hypertension, Bradycardia, irregular respirations", "rationale": "This is a late sign of high intracranial pressure."},
            {"q": "The 'Lethal Triad' in trauma is:", "options": ["Acidosis, Coagulopathy, Hypothermia", "Hypoxia, Hypotension, Acidosis", "Shock, Bleeding, Fever", "ALOC, Bradycardia, JVD"], "correct": "Acidosis, Coagulopathy, Hypothermia", "rationale": "These three conditions worsen each other and significantly increase mortality."},
            {"q": "Which criteria must ALL be met to rule out SMR?", "options": ["GCS 15, no midline pain, no neuro deficits, no distraction, no intoxication", "Walking, talking, alert, no bleeding", "Age > 18, no drugs, no fractures", "No neck pain, BP > 90, GCS 13"], "correct": "GCS 15, no midline pain, no neuro deficits, no distraction, no intoxication", "rationale": "Standard criteria for ruling out spinal motion restriction in blunt trauma."},
            {"q": "What is a flail chest?", "options": ["1 rib broken", "2+ ribs broken in 2+ places", "Sucking wound", "Paradoxical pulse"], "correct": "2+ ribs broken in 2+ places", "rationale": "Creates a free-floating segment of the chest wall that moves paradoxically."},
            {"q": "Priority for an open (sucking) chest wound:", "options": ["Pressure dressing", "Occlusive dressing (vented)", "CPAP", "Padded splint"], "correct": "Occlusive dressing (vented)", "rationale": "Prevents air from being trapped in the chest (tension pneumothorax)."},
            {"q": "Blood loss for a closed femur fracture is estimated at:", "options": ["100ml", "500ml", "1-1.5 Liters", "3 Liters"], "correct": "1-1.5 Liters", "rationale": "Significant internal bleeding occurs in the large muscles of the thigh."},
            {"q": "Primary blast injury causes barotrauma to:", "options": ["Bones", "Skin", "Hollow organs", "Limbs"], "correct": "Hollow organs", "rationale": "Pressure waves damage air-filled organs like lungs, ears, and GI tract."},
            {"q": "What is the hallmark sign of a tension pneumothorax?", "options": ["Tracheal deviation", "Tachycardia", "Increased breath sounds", "Fever"], "correct": "Tracheal deviation", "rationale": "Pressure pushes the mediastinum and trachea toward the unaffected side."},
            {"q": "A patient coughing up 'rust-colored' sputum likely has:", "options": ["Pneumonia", "CHF", "Tuberculosis", "Pulmonary Embolism"], "correct": "Pneumonia", "rationale": "Specifically pneumococcal pneumonia."},
            {"q": "Pink, frothy sputum is a classic sign of:", "options": ["High-altitude pulmonary edema (HAPE)", "Asthma", "COPD", "Pneumonia"], "correct": "High-altitude pulmonary edema (HAPE)", "rationale": "Indicative of fluid in the alveoli."},
            {"q": "Which category of shock includes tension pneumothorax and cardiac tamponade?", "options": ["Hypovolemic", "Cardiogenic", "Obstructive", "Distributive"], "correct": "Obstructive", "rationale": "A physical obstruction prevents blood from filling the heart or circulating properly."},
            {"q": "What is the primary concern with a 'Sucking Chest Wound'?", "options": ["Development of a Tension Pneumothorax", "External blood loss", "Infection", "Rib fractures"], "correct": "Development of a Tension Pneumothorax", "rationale": "Air enters the pleural space through the wound but cannot escape, building pressure."},
            {"q": "What is the landmark for needle decompression in a tension pneumothorax?", "options": ["2nd Intercostal space, mid-clavicular", "4th Intercostal space, mid-axillary", "5th Intercostal space, mid-clavicular", "Sub-xiphoid"], "correct": "2nd Intercostal space, mid-clavicular", "rationale": "This is the traditional site for relieving pressure in the pleural space (Advanced EMT/Paramedic skill)."},
            {"q": "In the 'Lethal Triad', why is hypothermia so dangerous?", "options": ["It impairs blood clotting (coagulopathy)", "It causes high blood pressure", "It stops the heart immediately", "It prevents infection"], "correct": "It impairs blood clotting (coagulopathy)", "rationale": "Clotting enzymes do not function at low body temperatures, worsening blood loss."},
            {"q": "A patient has a 'Steering Wheel' deformity and bruising on the chest. You should suspect:", "options": ["Myocardial Contusion", "Abdominal Evisceration", "Closed Head Injury", "Femur Fracture"], "correct": "Myocardial Contusion", "rationale": "Blunt force trauma to the sternum can bruise the heart muscle."},
            {"q": "What is 'Commotio Cordis'?", "options": ["Cardiac arrest caused by a blunt blow to the chest", "A type of heart attack", "Fluid around the heart", "A ruptured aorta"], "correct": "Cardiac arrest caused by a blunt blow to the chest", "rationale": "A sudden blow during a specific part of the heart's rhythm can cause V-Fib."},
            {"q": "The 'Platinum 10 Minutes' refers to:", "options": ["The max time spent on scene with a trauma patient", "The time it takes to get to the hospital", "The time to apply a tourniquet", "The duration of a primary survey"], "correct": "The max time spent on scene with a trauma patient", "rationale": "Critical trauma patients need surgery; scene time should be minimized."},
            {"q": "What is the first step in managing a patient with an evisceration?", "options": ["Cover with a moist, sterile dressing", "Push the organs back in", "Apply a dry pressure dressing", "Apply a tourniquet"], "correct": "Cover with a moist, sterile dressing", "rationale": "Never replace organs. Keep them moist and warm with sterile saline and an occlusive cover."},
            {"q": "A patient with a head injury has a BP of 190/110 and a HR of 50. This is:", "options": ["Cushing's Triad", "Beck's Triad", "Shock", "Anaphylaxis"], "correct": "Cushing's Triad", "rationale": "High BP and low HR are signs of herniation/high intracranial pressure."},
            {"q": "What is 'Paradoxical Motion' in a flail chest?", "options": ["The injured segment moves opposite the rest of the chest", "Both sides of the chest move together", "The patient stops breathing", "The stomach expands instead of the chest"], "correct": "The injured segment moves opposite the rest of the chest", "rationale": "The floating segment sinks in on inhalation and bulges out on exhalation."},
            {"q": "How should an impaled object in the cheek be handled if it obstructs the airway?", "options": ["Remove it", "Stabilize it in place", "Push it further in", "Cut it shorter"], "correct": "Remove it", "rationale": "Cheek impalements are the exception; remove if they block the airway or prevent ventilation."},
            {"q": "Which type of burn involves only the epidermis?", "options": ["Superficial (1st degree)", "Partial-thickness (2nd degree)", "Full-thickness (3rd degree)", "4th degree"], "correct": "Superficial (1st degree)", "rationale": "Example: A standard sunburn."},
            {"q": "Which type of burn presents with blisters?", "options": ["Partial-thickness (2nd degree)", "Superficial", "Full-thickness", "None"], "correct": "Partial-thickness (2nd degree)", "rationale": "Blistering is the hallmark of a 2nd-degree burn."},
            {"q": "Using the 'Rule of Nines,' the entire front of an adult's torso is:", "options": ["18%", "9%", "36%", "4.5%"], "correct": "18%", "rationale": "9% for the chest and 9% for the abdomen."},
            {"q": "What is the primary treatment for a chemical burn to the eyes?", "options": ["Immediate and continuous irrigation", "Applying a dry patch", "Neutralizing with another chemical", "Applying ointment"], "correct": "Immediate and continuous irrigation", "rationale": "Flush for at least 20 minutes with water or saline."},
            {"q": "In a blast injury, 'Secondary' injuries are caused by:", "options": ["Flying debris and shrapnel", "The pressure wave", "The patient being thrown", "Inhaled smoke"], "correct": "Flying debris and shrapnel", "rationale": "Primary is the wave; Secondary is shrapnel; Tertiary is the body hitting the ground."},
            {"q": "What is the purpose of a Traction Splint?", "options": ["Realign a mid-shaft femur fracture", "Stop bleeding", "Fix a hip dislocation", "Treat a knee injury"], "correct": "Realign a mid-shaft femur fracture", "rationale": "It prevents muscle spasms from grinding bone ends together."},
            {"q": "Which injury is a contraindication for a traction splint?", "options": ["Ankle or knee injury on the same leg", "Femur fracture", "Deformed thigh", "Closed fracture"], "correct": "Ankle or knee injury on the same leg", "rationale": "You cannot pull traction through a broken ankle or knee."},
            {"q": "A tourniquet should be applied:", "options": ["2-3 inches proximal to the wound", "Directly over the wound", "Distal to the wound", "Only on the neck"], "correct": "2-3 inches proximal to the wound", "rationale": "Place between the wound and the heart, but not over a joint."},
            {"q": "What is 'Battle’s Sign'?", "options": ["Bruising behind the ears", "Bruising around the eyes", "Fluid from the nose", "Unequal pupils"], "correct": "Bruising behind the ears", "rationale": "A late sign of a basilar skull fracture."},
            {"q": "What are 'Raccoon Eyes'?", "options": ["Bruising around the eyes", "Bruising behind the ears", "Redness of the eyes", "Swelling of the eyelids"], "correct": "Bruising around the eyes", "rationale": "Another sign of a basilar skull fracture."},
            {"q": "A patient has a traumatic amputation. How should the part be transported?", "options": ["Wrapped in sterile gauze, in a plastic bag, on ice", "Placed directly on dry ice", "Placed in a bucket of water", "Kept in the patient's pocket"], "correct": "Wrapped in sterile gauze, in a plastic bag, on ice", "rationale": "Keep it cool but do not let it freeze or get waterlogged."},
            {"q": "Define 'Ecchymosis':", "options": ["Bruising", "Swelling", "Redness", "Open wound"], "correct": "Bruising", "rationale": "Discoloration of the skin caused by internal bleeding."},
            {"q": "What is the 'Golden Hour'?", "options": ["The time from injury to definitive surgical care", "The first hour on scene", "The time to get a pulse back", "The time until a patient dies"], "correct": "The time from injury to definitive surgical care", "rationale": "The window in which survival rates are highest for major trauma."},
            {"q": "A 'GCS' of 3 indicates:", "options": ["Deep coma or death", "Normal consciousness", "Mild confusion", "Moderate brain injury"], "correct": "Deep coma or death", "rationale": "3 is the lowest possible score; 15 is the highest."},
            {"q": "The 'E' in GCS stands for 'Eye Opening'. What is the max score?", "options": ["4", "5", "6", "10"], "correct": "4", "rationale": "Eye (4), Verbal (5), Motor (6)."},
            {"q": "The 'V' in GCS stands for 'Verbal Response'. What is the max score?", "options": ["5", "4", "6", "15"], "correct": "5", "rationale": "Eye (4), Verbal (5), Motor (6)."},
            {"q": "The 'M' in GCS stands for 'Motor Response'. What is the max score?", "options": ["6", "4", "5", "10"], "correct": "6", "rationale": "Eye (4), Verbal (5), Motor (6)."},
            {"q": "A 'Point Tenderness' over the spine indicates a high risk for:", "options": ["Spinal Cord Injury", "Muscular strain", "Abdominal pain", "Internal bleeding"], "correct": "Spinal Cord Injury", "rationale": "Midline tenderness is a significant indicator for SMR."},
            {"q": "What is 'Subcutaneous Emphysema'?", "options": ["Air trapped under the skin", "Blood under the skin", "A type of infection", "Fluid in the lungs"], "correct": "Air trapped under the skin", "rationale": "Feels like 'Rice Krispies' crackling under the skin; indicates air escaping the airway/lungs."},
            {"q": "If a trauma patient has a 'Distracting Injury', can you rule out SMR?", "options": ["No", "Yes", "Only if they are 18", "Only if there is no blood"], "correct": "No", "rationale": "Pain from another injury can mask the pain of a spinal fracture."},
            {"q": "The primary cause of 'Distributive Shock' in trauma is:", "options": ["Spinal cord injury (Neurogenic)", "Blood loss", "Heart failure", "Tension pneumothorax"], "correct": "Spinal cord injury (Neurogenic)", "rationale": "Loss of nervous system control causes widespread vasodilation."},
            {"q": "Traumatic Asphyxia is caused by:", "options": ["Severe compression of the chest", "Choking on food", "A neck injury", "Low oxygen environment"], "correct": "Severe compression of the chest", "rationale": "Forceful compression causes blood to back up into the head and neck."},
            {"q": "What is the 'Rule of Palms'?", "options": ["The patient's palm is ~1% of their BSA", "Use your palm to check for heat", "Apply pressure with the palm", "Measure wounds by palm width"], "correct": "The patient's palm is ~1% of their BSA", "rationale": "Used to estimate the size of irregular burns."},
            {"q": "A 'Sucking Chest Wound' is also called:", "options": ["Open Pneumothorax", "Tension Pneumothorax", "Hemothorax", "Flail Chest"], "correct": "Open Pneumothorax", "rationale": "An open hole in the chest wall."},
            {"q": "What is 'Hemoptysis'?", "options": ["Coughing up blood", "Vomiting blood", "Blood in the urine", "Nosebleed"], "correct": "Coughing up blood", "rationale": "Commonly seen in lung trauma or infections."},
            {"q": "What is 'Hematemesis'?", "options": ["Vomiting blood", "Coughing up blood", "Blood in the stool", "Bruising"], "correct": "Vomiting blood", "rationale": "Indicates upper GI bleeding or swallowed blood from trauma."},
            {"q": "A 'Traumatic Brain Injury' with a period of lucidity followed by rapid decline is:", "options": ["Epidural Hematoma", "Subdural Hematoma", "Concussion", "Contusion"], "correct": "Epidural Hematoma", "rationale": "Classic presentation: Knocked out, wakes up, then crashes as arterial bleeding builds pressure."},
            {"q": "Which hematoma is typically a 'Slow' venous bleed?", "options": ["Subdural Hematoma", "Epidural Hematoma", "Intracerebral", "Subarachnoid"], "correct": "Subdural Hematoma", "rationale": "Venous bleeding under the dura mater; symptoms can take days or weeks to appear."},
            {"q": "A patient with a traumatic amputation should have a tourniquet applied:", "options": ["Immediately to stop life-threatening bleeding", "Only after a pressure dressing fails", "Only by a doctor", "Never"], "correct": "Immediately to stop life-threatening bleeding", "rationale": "Amputations are immediate priorities for tourniquet use."},
            {"q": "The most common cause of 'Obstructive Shock' in trauma is:", "options": ["Tension Pneumothorax", "Gunshot wound", "Broken ribs", "Concussion"], "correct": "Tension Pneumothorax", "rationale": "Pressure on the heart and great vessels blocks blood flow."},
            # NOTE: Include all remaining questions from the Trauma_Review document here.
        ]
    
        
        # --- PASTE BATCHES 1, 2, AND 3 ABOVE THIS LINE ---
    }

# ==========================================
# PART 2: APP ENGINE
# ==========================================
st.set_page_config(layout="wide", page_title="EMT Study Pro", page_icon="🚑")

# Initialize session state for data persistence
if 'all_data' not in st.session_state:
    st.session_state.all_data = get_all_questions()
    if "PLACEHOLDER" in st.session_state.all_data:
        del st.session_state.all_data["PLACEHOLDER"]
    st.session_state.quiz_list = []
    st.session_state.user_answers = {}
    st.session_state.submitted = False

with st.sidebar:
    st.header("⚙️ Quiz Settings")
    
    # 1. Module Selection
    available_modules = list(st.session_state.all_data.keys())
    selected_modules = st.multiselect(
        "Select Study Modules:",
        options=available_modules,
        default=available_modules
    )
    
    # 2. Randomization Toggle
    is_random = st.toggle("Shuffle Question Order", value=True)
    
    # 3. Fixed Quiz Sizes
    quiz_size = st.selectbox(
        "Number of Questions:",
        options=[20, 30, 50, 60],
        index=0
    )
    
    if st.button("🚀 Generate Quiz", type="primary"):
        pool = []
        for mod in selected_modules:
            pool.extend(st.session_state.all_data[mod])
        
        if not pool:
            st.warning("Please select at least one module.")
        else:
            if is_random:
                random.shuffle(pool)
            
            # Pull the requested size, or the whole pool if it's smaller than the size
            st.session_state.quiz_list = pool[:min(len(pool), quiz_size)]
            st.session_state.user_answers = {}
            st.session_state.submitted = False
            st.rerun()

st.title("🚑 EMT Knowledge Master")

if not st.session_state.quiz_list:
    st.info("👈 Use the sidebar to select your modules and quiz size, then click 'Generate Quiz'.")
else:
    st.caption(f"Reviewing {len(st.session_state.quiz_list)} questions from: {', '.join(selected_modules)}")
    
    with st.form("quiz_form"):
        for idx, item in enumerate(st.session_state.quiz_list):
            st.subheader(f"Question {idx+1}")
            st.write(item['q'])
            
            st.session_state.user_answers[idx] = st.radio(
                f"Select for Q{idx+1}:",
                options=item['options'],
                key=f"q_{idx}",
                index=None
            )
            st.divider()
            
        submit_btn = st.form_submit_button("Submit and Grade")

    if submit_btn:
        st.session_state.submitted = True
        score = 0
        for idx, item in enumerate(st.session_state.quiz_list):
            user_choice = st.session_state.user_answers.get(idx)
            correct_ans = item['correct']
            
            if user_choice == correct_ans:
                score += 1
                st.success(f"✅ Q{idx+1}: Correct!")
            else:
                st.error(f"❌ Q{idx+1}: Incorrect. Correct: {correct_ans}")
            
            st.info(f"**Rationale:** {item['rationale']}")
        
        final_pct = (score / len(st.session_state.quiz_list)) * 100
        st.metric("Final Score", f"{final_pct:.1f}%", f"{score}/{len(st.session_state.quiz_list)}")
        
        if final_pct >= 80:
            st.balloons()