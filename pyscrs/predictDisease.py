import pickle
import pandas as pd
import numpy as np

def predictThis(symp1, symp2, symp3, symp4, symp5, symp6, symp7, symp8, symp9, symp10, symp11, symp12, symp13, symp14, symp15, symp16, symp17):
    model = pickle.load(open("data/diseasePredictModel.pkl", "rb"))
    featureCategories = ['vomiting','fatigue','itching','skin_rash','chills','joint_pain','continuous_sneezing','headache','acidity','stomach_pain','constipation','muscle_weakness','burning_micturition','muscle_wasting','back_pain','bladder_discomfort','weight_gain','breathlessness','yellowish_skin','weakness_in_limbs','chest_pain','cough','sunken_eyes','patches_in_throat','indigestion','shivering','pain_during_bowel_movements','cramps','weight_loss','mood_swings','neck_pain','stiff_neck','pus_filled_pimples','high_fever','dehydration','weakness_of_one_body_side','dizziness','sweating','blister','nausea','nodal_skin_eruptions','ulcers_on_tongue','foul_smell_ofurine','cold_hands_and_feets','blackheads','loss_of_appetite','restlessness','skin_peeling','pain_in_anal_region','swelling_joints','anxiety','lethargy','bruising','abdominal_pain','knee_pain','diarrhoea','watering_from_eyes','continuous_feel_of_urine','altered_sensorium','dischromic_patches','loss_of_balance','red_sore_around_nose','extra_marital_contacts','scurring','blurred_and_distorted_vision','dark_urine','silver_like_dusting','swelling_of_stomach','obesity','bloody_stool','movement_stiffness','hip_joint_pain','spinning_movements','None','lack_of_concentration','spotting_urination','family_history','passage_of_gases','yellow_crust_ooze','distention_of_abdomen','painful_walking','excessive_hunger','irregular_sugar_level','swollen_legs','small_dents_in_nails','yellowing_of_eyes','irritation_in_anus','internal_itching','mucoid_sputum','unsteadiness','history_of_alcohol_consumption','swollen_blood_vessels','inflammatory_nails','prominent_veins_on_calf','puffy_face_and_eyes','fluid_overload','malaise','fast_heart_rate','depression','swelled_lymph_nodes','muscle_pain','enlarged_thyroid','yellow_urine','mild_fever','phlegm','irritability','visual_disturbances','increased_appetite','brittle_nails','drying_and_tingling_lips','throat_irritation','swollen_extremeties','slurred_speech','polyuria','toxic_look_(typhos)','pain_behind_the_eyes','red_spots_over_body','receiving_blood_transfusion','redness_of_eyes','rusty_sputum','abnormal_menstruation','belly_pain','acute_liver_failure','coma','receiving_unsterile_injections','sinus_pressure','palpitations','stomach_bleeding','runny_nose','congestion','blood_in_sputum','loss_of_smell']
    diseaseCategory = ['(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne',
       'Alcoholic hepatitis', 'Allergy', 'Arthritis', 'Bronchial Asthma',
       'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis',
       'Common Cold', 'Dengue', 'Diabetes ',
       'Dimorphic hemmorhoids(piles)', 'Drug Reaction',
       'Fungal infection', 'GERD', 'Gastroenteritis', 'Heart attack',
       'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
       'Hypertension ', 'Hyperthyroidism', 'Hypoglycemia',
       'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine',
       'Osteoarthristis', 'Paralysis (brain hemorrhage)',
       'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis', 'Tuberculosis',
       'Typhoid', 'Urinary tract infection', 'Varicose veins',
       'hepatitis A']
    
    symp1 = featureCategories.index(symp1) + 1
    symp2 = featureCategories.index(symp2) + 1
    symp3 = featureCategories.index(symp3) + 1
    symp4 = featureCategories.index(symp4) + 1
    symp5 = featureCategories.index(symp5) + 1
    symp6 = featureCategories.index(symp6) + 1
    symp7 = featureCategories.index(symp7) + 1
    symp8 = featureCategories.index(symp8) + 1
    symp9 = featureCategories.index(symp9) + 1
    symp10 = featureCategories.index(symp10) + 1
    symp11 = featureCategories.index(symp11) + 1
    symp12 = featureCategories.index(symp12) + 1
    symp13 = featureCategories.index(symp13) + 1
    symp14 = featureCategories.index(symp14) + 1
    symp15 = featureCategories.index(symp15) + 1
    symp16 = featureCategories.index(symp16) + 1
    symp17 = featureCategories.index(symp17) + 1
    
    predictedValue = model.predict([[symp1, symp2, symp3, symp4, symp5, symp6, symp7, symp8, symp9, symp10, symp11, symp12, symp13, symp14, symp15, symp16, symp17]])

    predictedDisease = diseaseCategory[predictedValue[0]]

    return predictedDisease

def getDescription(disease):
    df_Descript = pd.read_csv("data/diseaseData/symptom_Description.csv")
    return df_Descript[df_Descript["Disease"] == disease]["Description"].values[0]

def getPrecautions(disease):
    df_precaution = pd.read_csv("data/diseaseData/symptom_precaution.csv")
    df_precaution.fillna("None", inplace=True)
    precs = df_precaution[df_precaution["Disease"] == disease].values[0]
    precautions = []
    for stuff in precs:
        if stuff == "None":
            pass
        else:
            precautions.append(stuff)
    
    return precautions

def getDiseasesAndDescription():
    df_Descript = pd.read_csv("data/diseaseData/symptom_Description.csv")
    diseases = df_Descript["Disease"].values
    descriptions = df_Descript["Description"].values
    return diseases, descriptions

def getDiseasesAndPrecautions():
    df_precaution = pd.read_csv("data/diseaseData/symptom_precaution.csv")
    df_precaution.fillna("None", inplace=True)
    return df_precaution.values