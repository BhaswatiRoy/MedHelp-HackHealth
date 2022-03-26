import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model1 = pickle.load(open('diabetesmodel.pkl', 'rb'))
model2 = pickle.load(open('covid19model.pkl', 'rb'))
model3 = pickle.load(open('heartdiseasemodel.pkl', 'rb'))

#home page

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

#diabetes app
@app.route('/d')
def d():
    return render_template('diabetesindex.html')
@app.route('/c')
def c():
    return render_template('covid19index.html')
@app.route('/h')
def h():
    return render_template('heartdiseaseindex.html')
@app.route('/m')
def m():
    return render_template('medicalsuggestions.html')
@app.route('/di',methods=['POST'])
def diabetespredict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model1.predict(final_features)
    if prediction=='No':
        data="Not Affected By Diabetes"
    elif prediction=="Yes":
        data="Affected By Diabetes"
    return render_template('diabetesindex.html', prediction_text1='Health Status: {}'.format(data))

#covid-19 app

@app.route('/ci',methods=['POST'])
def covid19predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)
    if prediction==0:
        data="Not Affected By Covid-19"
    elif prediction==1:
        data="Affected By Covid-19"
    return render_template('covid19index.html', prediction_text2='Health Status: {}'.format(data))

#heart disease app

@app.route('/hi',methods=['POST'])
def heartdiseasepredict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model3.predict(final_features)
    if prediction=="Absence":
        data="Not Affected By Heart Disease"
    elif prediction=="Presence":
        data="Affected By Heart Disease"
    return render_template('heartdiseaseindex.html', prediction_text3='Health Status: {}'.format(data))

if __name__ == "__main__":
    app.run(debug=True)
