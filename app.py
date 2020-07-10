# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:26:57 2020

@author: Data Science Learn
"""

import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('cardiology-model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if(request.method == 'POST'):
        
        #Age
        age = int(request.form['age'])
        
        #Sex
        sex = request.form['sex']
        if(sex =='Male'):
            sex=1
        else:
            sex=0
        
        #chest_pain_type
        chest_pain_type = request.form['chest_pain_type']
        if(chest_pain_type == 'asymptomatic'):
            chest_pain_type_atypical_angina = 0
            chest_pain_type_non_anginal_pain = 0
            chest_pain_type_typical_angina = 0
        elif(chest_pain_type == 'typical-angina'):
            chest_pain_type_atypical_angina = 0
            chest_pain_type_non_anginal_pain = 0
            chest_pain_type_typical_angina = 1
        elif(chest_pain_type == 'atypical-angina'):
            chest_pain_type_atypical_angina = 1
            chest_pain_type_non_anginal_pain = 0
            chest_pain_type_typical_angina = 0
        else:
            chest_pain_type_atypical_angina = 0
            chest_pain_type_non_anginal_pain = 1
            chest_pain_type_typical_angina = 0
        
        #resting_blood_pressure
        resting_blood_pressure=int(request.form['resting_blood_pressure'])
        
        #cholesterol
        cholesterol = float(request.form['cholesterol'])
        
        #fasting_blood_sugar
        fasting_blood_sugar = request.form['fasting_blood_sugar']
        if(fasting_blood_sugar == 'greater-than-120'):
            fasting_blood_sugar=1
        else:
            fasting_blood_sugar=0
        
        #rest_ecg
        rest_ecg = request.form['rest_ecg']
        if(rest_ecg == 'normal'):
            rest_ecg = 0
        elif(rest_ecg == 'wave-abnormality'):
            rest_ecg = 1
        else:
            rest_ecg = 2
        
        #max_heart_rate_achieved
        max_heart_rate_achieved = float(request.form['max_heart_rate_achieved'])
        
        #exercise_induced_angina
        exercise_induced_angina = request.form['exercise_induced_angina']
        if(exercise_induced_angina =='yes'):
            exercise_induced_angina = 1
        else:
            exercise_induced_angina = 0
        
        #st_depression
        st_depression = float(request.form['st_depression'])
        
        #st_slope
        st_slope = request.form['st_slope']
        if(st_slope == 'upsloping'):
            st_slope = 1
        elif(st_slope == 'flat'):
            st_slope = 2
        else:
            st_slope = 3
        
        #num_major_vessels
        num_major_vessels = int(request.form['num_major_vessels'])
        if(num_major_vessels == 0):
            num_major_vessels = 0
        elif(num_major_vessels == 1):
            num_major_vessels = 1
        elif(num_major_vessels == 2):
            num_major_vessels = 2
        else:
            num_major_vessels = 3
        
        #thalassemia
        thalassemia = request.form['thalassemia']
        if(thalassemia == 'normal'):
            thalassemia = 1
        elif(thalassemia == 'fixed-defect'):
            thalassemia = 2
        else:
            thalassemia = 3
        
        #Prediction
        output = model.predict([[age,
                                 sex,
                                 resting_blood_pressure,
                                 cholesterol,
                                 fasting_blood_sugar,
                                 rest_ecg,
                                 max_heart_rate_achieved,
                                 exercise_induced_angina,
                                 st_depression,
                                 st_slope,
                                 num_major_vessels,
                                 thalassemia,
                                 chest_pain_type_atypical_angina,
                                 chest_pain_type_non_anginal_pain,
                                 chest_pain_type_typical_angina]])
        #output=round(prediction[0],2)
        #output=np.argmax(output, axis=1)
        print(output)
        if output == 1:
            return render_template('index.html',prediction_text="Patient have the heart disease")
        else:
            return render_template('index.html',prediction_text="Patient does not have the heart disease")
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug = False)

