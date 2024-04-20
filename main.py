# app.py
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        pregnant = request.form.get('pregnant')
        duration_number = request.form.get('duration_number')
        duration_period = request.form.get('duration_period')
        symptom_scale = request.form.get('symptomscale')
        symptoms = request.form.get('symptoms')
        previous_diagnoses = request.form.get('previous_diagnoses')
        previous_surgeries = request.form.get('previous_surgeries')
        family_medical_history = request.form.get('family_medical_history')
        fitness_level = request.form.get('fitness_level')
        substances_alcohol = request.form.get('substances_alcohol')
        substances_cigarettes = request.form.get('substances_cigarettes')
        substances_text = request.form.get('substances_text')

        inp = "Patient Information:\nAge: "
        if age == None: inp = inp + "Not Specified\nGender: "
        else: inp = inp + age + "\nGender: "

        if gender == None: inp = inp + "Not Specified\nIs Patient Pregnant? "
        else: inp = inp + gender + "\nIs Patient Pregnant? "

        if pregnant == None: inp = inp + "Not Specified\nNumerical Duration of Symptoms: "
        else: inp = inp + pregnant + "\nNumerical Duration of Symptoms: "

        if duration_number == None: inp = inp + "Not Specified\nTimespan of Symptoms: "
        else: inp = inp + duration_number + "\nTimespan Duration of Symptoms: "

        if duration_period == None: inp = inp + "Not Specified\nSeverity of Symptoms (on a scale from 1 to 10): "
        else: inp = inp + duration_period + "\nSeverity of Symptoms (on a scale from 1 to 10): "

        if symptom_scale == None: inp = inp + "Not Specified\nSymptoms: "
        else: inp = inp + symptom_scale + "\nSymptoms: "

        if symptoms == None: inp = inp + "Not Specified\nPrevious Diagnoses: "
        else: inp = inp + symptoms + "\nPrevious Diagnoses: "

        if previous_diagnoses == None: inp = inp + "Not Specified\nPrevious Surgeries: "
        else: inp = inp + previous_diagnoses + "\nPrevious Surgeries: "

        if previous_surgeries == None: inp = inp + "Not Specified\nFamily Medical History: "
        else: inp = inp + previous_surgeries + "\nFamily Medical History: "

        if family_medical_history == None: inp = inp + "Not Specified\nFitness Level: "
        else: inp = inp + family_medical_history + "\nFitness Level: "

        if fitness_level == None: inp = inp + "Not Specified\nSubstances Taken: "
        else: inp = inp + fitness_level + "\nSubstances Taken: "

        if substances_alcohol == None and substances_cigarettes == None and substances_text == None: inp = inp + "Not Specified\n"
        
        else:
            if substances_alcohol != None: inp = inp + substances_alcohol + ", "
            if substances_cigarettes != None: inp = inp + substances_cigarettes + ", "
            if substances_text != None: inp = inp + "Other: " + substances_text + ", "
            inp = inp[:len(inp) - 2]

        inp = inp + "\n At the beginning of your response, please specify that this is a preliminary diagnosis and that this is not a substitute for professional medical advice"

        print(inp)

        import ollama

        stream = ollama.chat(
            model='medllama2',
            messages=[{'role': 'user', 'content': inp}],
            stream=True,
        )

        response = "" 

        for chunk in stream:
            if '[' in chunk['message']['content']:
                break
            if (len(chunk['message']['content']) > 0 and (chunk['message']['content'][0] != '[')):
                print(chunk['message']['content'], end='', flush=True)
                response += str(chunk['message']['content'])


        return jsonify({"additional_text": response})

if __name__ == '__main__':
    app.run(debug=True)
