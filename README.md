<h1 align="center">
             MedHelp HackHealth 🩺 💊 💉
</h1>
  
  ![image](https://user-images.githubusercontent.com/78029145/153434524-ca6c416b-3f8e-43ca-8174-6f68789209a5.png)

This app is used to predict the current medical state of an individual and also includes a section which will provide some medical guidelines to anyone who is affected by any common disease from the disease prediction section.

The disease sections include ->

**1. Covid-19**

**2. Diabetes**

**3. Heart Disease**

## Tech Stacks Used

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

## Libraries Used

<img src="https://img.shields.io/badge/numpy%20-%2314354C.svg?&style=for-the-badge&logo=numpy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas%20-%2314354C.svg?&style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/pickle%20-%2314354C.svg?&style=for-the-badge&logo=pickle&logoColor=white"/>
<img src="https://img.shields.io/badge/flask%20-%2314354C.svg?&style=for-the-badge&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/scikitlearn%20-%2314354C.svg?&style=for-the-badge&logo=scikitlearn&logoColor=white"/> <img src="https://img.shields.io/badge/html%20-%2314354C.svg?&style=for-the-badge&logo=html&logoColor=white"/> <img src="https://img.shields.io/badge/css%20-%2314354C.svg?&style=for-the-badge&logo=css&logoColor=white"/> <img src="https://img.shields.io/badge/bootstrap%20-%2314354C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>

## Structure Of The Project

- The home page consists of cards which contains the links to 4 different web pages in which 3 are medical prediction section and 1 is medical guideline section.
- The prediction sections include - Diabetes Prediction, Covid-19 Prediction, Heart Disease Prediction.
- Each prediction page is conneceted with a Machine Learning Model which uses Random Forest Classifier to predict whether the user is affected by that disease or not.
- Also we have 3 different datasets used for training each of the machine learning model. The models are then stored in a pickle file and connected with the web pages using Flask.
- Each of the 3 web pages associated with prediction contains forms which take 4 different feature as input from the user in a given specified range in number format.
- The value entered in the forms are then fed into each of the individual models for getting the prediction. According to the predicted values the user is alerted whether they are a victim to that disease or not.
- The most relevant features are taken into consideration for prediction also these features can be found out with simple tests or analysis without visiting any doctor.
- So the victim can get a broad overview of their health condition specially regarding 3 most common diseases without any kind of doctor appointments.

## The features taken into consideration

| Disease | Features |
| - | - |
| Covid-19 | Dry Cough, Fever, Sore Throat, Breathing Problem |
| Diabetes | Glucose, Insulin, Body Mass Index(BMI), Age |
| Heart Disease | Chest Pain, Blood Pressure(BP), Cholestrol, Max Heart Rate(HR) |

The feature selection is carefully done under the supervision of a medical science student.
