from flask import Flask, render_template, url_for, request
from pyscrs import predictDisease

app = Flask("__name__")
app.secret_key = "437437437437"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/symptoms", methods=["POST", "GET"])
def getUserSymptoms():
    symp1Vals = ['itching', 'skin_rash', 'continuous_sneezing', 'shivering',
       'stomach_pain', 'acidity', 'vomiting', 'indigestion',
       'muscle_wasting', 'patches_in_throat', 'fatigue', 'weight_loss',
       'sunken_eyes', 'cough', 'headache', 'chest_pain', 'back_pain',
       'weakness_in_limbs', 'chills', 'joint_pain', 'yellowish_skin',
       'constipation', 'pain_during_bowel_movements', 'breathlessness',
       'cramps', 'weight_gain', 'mood_swings', 'neck_pain',
       'muscle_weakness', 'stiff_neck', 'pus_filled_pimples',
       'burning_micturition', 'bladder_discomfort', 'high_fever']

    symp2Vals = ['skin_rash', 'nodal_skin_eruptions', 'shivering', 'chills',
    'acidity', 'ulcers_on_tongue', 'vomiting', 'yellowish_skin',
    'stomach_pain', 'loss_of_appetite', 'indigestion',
    'patches_in_throat', 'high_fever', 'weight_loss', 'restlessness',
    'sunken_eyes', 'dehydration', 'cough', 'chest_pain', 'dizziness',
    'headache', 'weakness_in_limbs', 'neck_pain',
    'weakness_of_one_body_side', 'fatigue', 'joint_pain', 'lethargy',
    'nausea', 'abdominal_pain', 'pain_during_bowel_movements',
    'pain_in_anal_region', 'breathlessness', 'sweating', 'cramps',
    'bruising', 'weight_gain', 'cold_hands_and_feets', 'mood_swings',
    'anxiety', 'knee_pain', 'stiff_neck', 'swelling_joints',
    'pus_filled_pimples', 'blackheads', 'bladder_discomfort',
    'foul_smell_ofurine', 'skin_peeling', 'blister']

    symp3Vals = ['nodal_skin_eruptions', 'dischromic_patches', 'chills',
    'watering_from_eyes', 'ulcers_on_tongue', 'vomiting',
    'yellowish_skin', 'nausea', 'stomach_pain', 'burning_micturition',
    'abdominal_pain', 'loss_of_appetite', 'high_fever',
    'extra_marital_contacts', 'restlessness', 'lethargy',
    'dehydration', 'diarrhoea', 'breathlessness', 'dizziness',
    'loss_of_balance', 'headache', 'blurred_and_distorted_vision',
    'neck_pain', 'weakness_of_one_body_side', 'altered_sensorium',
    'fatigue', 'weight_loss', 'sweating', 'joint_pain', 'dark_urine',
    'swelling_of_stomach', 'cough', 'pain_in_anal_region',
    'bloody_stool', 'chest_pain', 'bruising', 'obesity',
    'cold_hands_and_feets', 'mood_swings', 'anxiety', 'knee_pain',
    'hip_joint_pain', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'blackheads', 'scurring',
    'foul_smell_ofurine', 'continuous_feel_of_urine', 'skin_peeling',
    'silver_like_dusting', 'blister', 'red_sore_around_nose']

    symp4Vals = ['dischromic_patches', 'None', 'watering_from_eyes', 'vomiting',
    'cough', 'nausea', 'loss_of_appetite', 'burning_micturition',
    'spotting_urination', 'passage_of_gases', 'abdominal_pain',
    'extra_marital_contacts', 'lethargy', 'irregular_sugar_level',
    'diarrhoea', 'breathlessness', 'family_history', 'loss_of_balance',
    'lack_of_concentration', 'blurred_and_distorted_vision',
    'excessive_hunger', 'dizziness', 'altered_sensorium',
    'weight_loss', 'high_fever', 'sweating', 'headache', 'fatigue',
    'dark_urine', 'yellowish_skin', 'yellowing_of_eyes',
    'swelling_of_stomach', 'distention_of_abdomen', 'bloody_stool',
    'irritation_in_anus', 'chest_pain', 'obesity', 'swollen_legs',
    'mood_swings', 'restlessness', 'hip_joint_pain', 'swelling_joints',
    'movement_stiffness', 'painful_walking', 'spinning_movements',
    'scurring', 'continuous_feel_of_urine', 'silver_like_dusting',
    'small_dents_in_nails', 'red_sore_around_nose',
    'yellow_crust_ooze']

    symp5Vals = ['None', 'cough', 'chest_pain', 'loss_of_appetite',
    'abdominal_pain', 'spotting_urination', 'internal_itching',
    'passage_of_gases', 'irregular_sugar_level',
    'blurred_and_distorted_vision', 'family_history', 'mucoid_sputum',
    'lack_of_concentration', 'excessive_hunger', 'stiff_neck',
    'loss_of_balance', 'high_fever', 'yellowish_skin', 'headache',
    'nausea', 'fatigue', 'dark_urine', 'yellowing_of_eyes',
    'distention_of_abdomen', 'history_of_alcohol_consumption',
    'breathlessness', 'sweating', 'irritation_in_anus', 'swollen_legs',
    'swollen_blood_vessels', 'lethargy', 'dizziness', 'diarrhoea',
    'swelling_joints', 'painful_walking', 'unsteadiness',
    'small_dents_in_nails', 'inflammatory_nails', 'yellow_crust_ooze']

    symp6Vals = ['None', 'chest_pain', 'abdominal_pain', 'yellowing_of_eyes',
    'internal_itching', 'blurred_and_distorted_vision', 'obesity',
    'mucoid_sputum', 'stiff_neck', 'depression', 'yellowish_skin',
    'dark_urine', 'nausea', 'diarrhoea', 'headache',
    'loss_of_appetite', 'high_fever', 'constipation', 'family_history',
    'history_of_alcohol_consumption', 'fluid_overload',
    'breathlessness', 'swelled_lymph_nodes', 'sweating', 'malaise',
    'swollen_blood_vessels', 'prominent_veins_on_calf', 'dizziness',
    'puffy_face_and_eyes', 'fast_heart_rate', 'painful_walking',
    'unsteadiness', 'inflammatory_nails']

    symp7Vals = ['None', 'yellowing_of_eyes', 'obesity', 'excessive_hunger',
    'depression', 'irritability', 'dark_urine', 'abdominal_pain',
    'muscle_pain', 'diarrhoea', 'loss_of_appetite', 'mild_fever',
    'headache', 'nausea', 'constipation', 'yellow_urine',
    'fluid_overload', 'breathlessness', 'sweating',
    'swelled_lymph_nodes', 'malaise', 'phlegm',
    'prominent_veins_on_calf', 'puffy_face_and_eyes',
    'enlarged_thyroid', 'fast_heart_rate',
    'blurred_and_distorted_vision']

    symp8Vals = ['None', 'excessive_hunger', 'increased_appetite', 'irritability',
    'visual_disturbances', 'abdominal_pain', 'muscle_pain',
    'mild_fever', 'swelled_lymph_nodes', 'nausea', 'loss_of_appetite',
    'diarrhoea', 'yellow_urine', 'yellowing_of_eyes', 'sweating',
    'malaise', 'phlegm', 'chest_pain', 'enlarged_thyroid',
    'brittle_nails', 'muscle_weakness', 'drying_and_tingling_lips']

    symp9Vals = ['None', 'increased_appetite', 'polyuria', 'visual_disturbances',
    'swelled_lymph_nodes', 'malaise', 'loss_of_appetite',
    'pain_behind_the_eyes', 'toxic_look_(typhos)', 'diarrhoea',
    'mild_fever', 'yellowing_of_eyes', 'abdominal_pain', 'phlegm',
    'throat_irritation', 'fast_heart_rate', 'chest_pain',
    'brittle_nails', 'swollen_extremeties', 'muscle_weakness',
    'irritability', 'slurred_speech', 'drying_and_tingling_lips']

    symp10Vals = ['None', 'polyuria', 'malaise', 'red_spots_over_body',
    'pain_behind_the_eyes', 'back_pain', 'belly_pain',
    'toxic_look_(typhos)', 'yellowing_of_eyes', 'muscle_pain',
    'receiving_blood_transfusion', 'acute_liver_failure', 'mild_fever',
    'throat_irritation', 'redness_of_eyes', 'rusty_sputum',
    'fast_heart_rate', 'swollen_extremeties', 'depression',
    'irritability', 'abnormal_menstruation', 'slurred_speech']

    symp11Vals = ['None', 'red_spots_over_body', 'back_pain', 'malaise',
    'belly_pain', 'muscle_pain', 'receiving_blood_transfusion',
    'receiving_unsterile_injections', 'coma', 'acute_liver_failure',
    'yellowing_of_eyes', 'swelled_lymph_nodes', 'redness_of_eyes',
    'sinus_pressure', 'rusty_sputum', 'depression', 'irritability',
    'abnormal_menstruation', 'palpitations']

    symp12Vals = ['None', 'muscle_pain', 'malaise', 'receiving_unsterile_injections',
    'stomach_bleeding', 'coma', 'swelled_lymph_nodes',
    'sinus_pressure', 'runny_nose', 'irritability',
    'abnormal_menstruation', 'palpitations']

    symp13Vals = ['None', 'red_spots_over_body', 'muscle_pain', 'stomach_bleeding',
    'malaise', 'phlegm', 'runny_nose', 'congestion',
    'abnormal_menstruation']

    symp14Vals = ['None', 'red_spots_over_body', 'phlegm', 'chest_pain',
    'congestion']

    symp15Vals = ['None', 'chest_pain', 'blood_in_sputum', 'loss_of_smell']

    symp16Vals = ['None', 'blood_in_sputum', 'loss_of_smell', 'muscle_pain']

    symp17Vals = ['None', 'muscle_pain']



    userName = request.form["USRNAME"]
    if request.method == 'POST':
        return render_template("getSymptoms.html", userName=userName, 
                                            symp1Vals=symp1Vals, symp1Len=len(symp1Vals),
                                            symp2Vals=symp2Vals, symp2Len=len(symp2Vals),
                                            symp3Vals=symp3Vals, symp3Len=len(symp3Vals),
                                            symp4Vals=symp4Vals, symp4Len=len(symp4Vals),
                                            symp5Vals=symp5Vals, symp5Len=len(symp5Vals),
                                            symp6Vals=symp6Vals, symp6Len=len(symp6Vals),
                                            symp7Vals=symp7Vals, symp7Len=len(symp7Vals),
                                            symp8Vals=symp8Vals, symp8Len=len(symp8Vals),
                                            symp9Vals=symp9Vals, symp9Len=len(symp9Vals),
                                            symp10Vals=symp10Vals, symp10Len=len(symp10Vals),
                                            symp11Vals=symp11Vals, symp11Len=len(symp11Vals),
                                            symp12Vals=symp12Vals, symp12Len=len(symp12Vals),
                                            symp13Vals=symp13Vals, symp13Len=len(symp13Vals),
                                            symp14Vals=symp14Vals, symp14Len=len(symp14Vals),
                                            symp15Vals=symp15Vals, symp15Len=len(symp15Vals),
                                            symp16Vals=symp16Vals, symp16Len=len(symp16Vals),
                                            symp17Vals=symp17Vals, symp17Len=len(symp17Vals),
        )

@app.route("/predictedDisease", methods=["POST"])
def predictedDisease():
    if request.method == "POST":
        usrSymp1 = request.form["SYMP1"]
        usrSymp2 = request.form["SYMP2"]
        usrSymp3 = request.form["SYMP3"]
        usrSymp4 = request.form["SYMP4"]
        usrSymp5 = request.form["SYMP5"]
        usrSymp6 = request.form["SYMP6"]
        usrSymp7 = request.form["SYMP7"]
        usrSymp8 = request.form["SYMP8"]
        usrSymp9 = request.form["SYMP9"]
        usrSymp10 = request.form["SYMP10"]
        usrSymp11 = request.form["SYMP11"]
        usrSymp12 = request.form["SYMP12"]
        usrSymp13 = request.form["SYMP13"]
        usrSymp14 = request.form["SYMP14"]
        usrSymp15 = request.form["SYMP15"]
        usrSymp16 = request.form["SYMP16"]
        usrSymp17 = request.form["SYMP17"]

        usrName = request.form["USRNAME"]

        usrDisease = predictDisease.predictThis(usrSymp1, usrSymp2, usrSymp3, usrSymp4, usrSymp5, usrSymp6, usrSymp7, usrSymp8, usrSymp9, usrSymp10, usrSymp11, 
        usrSymp12, usrSymp13, usrSymp14, usrSymp15, usrSymp16, usrSymp17)

        diseaseDesc = predictDisease.getDescription(usrDisease)
        precautions = predictDisease.getPrecautions(usrDisease)

        return render_template("predictedResult.html", usrName=usrName, usrDisease=usrDisease, diseaseDesc=diseaseDesc,
                                precautions=precautions, lenPrecaution=len(precautions)
        )


@app.route("/displayDiseases")
def displayDiseases():
    diseases, descriptions = predictDisease.getDiseasesAndDescription()
    lenOfDisease = len(diseases)
    return render_template("diseases.html", diseases=diseases, descriptions=descriptions, lenOfDisease=lenOfDisease)

@app.route("/healthAdvices")
def healthAdvices():
    precautions = predictDisease.getDiseasesAndPrecautions()
    lenPrec = len(precautions)
    return render_template("precautions.html", precautions=precautions, lenPrec=lenPrec)


if __name__ == '__main__':
    app.run(debug=True)