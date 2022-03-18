<h1 align="center">
             MedHelp HackHealth 🩺 💊 💉
</h1>
  
  ![image](https://user-images.githubusercontent.com/78029145/153434524-ca6c416b-3f8e-43ca-8174-6f68789209a5.png)

## Overview of the App

This app is used to predict the current medical state of an individual regarding 3 most common diseases and also includes a section which will provide some medical guidelines to anyone who is affected by any common disease from the disease prediction section.

The disease sections include ->

**1. Covid-19**

**2. Diabetes**

**3. Heart Disease**

## Tech Stacks Used

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

## Libraries Used

<img src="https://img.shields.io/badge/numpy%20-%2314354C.svg?&style=for-the-badge&logo=numpy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas%20-%2314354C.svg?&style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/pickle%20-%2314354C.svg?&style=for-the-badge&logo=pickle&logoColor=white"/>
<img src="https://img.shields.io/badge/flask%20-%2314354C.svg?&style=for-the-badge&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/scikitlearn%20-%2314354C.svg?&style=for-the-badge&logo=scikitlearn&logoColor=white"/> <img src="https://img.shields.io/badge/html5%20-%2314354C.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/css3%20-%2314354C.svg?&style=for-the-badge&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/bootstrap%20-%2314354C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>

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
| Diabetes | Glucose, Insulin, Body Mass Index, Age |
| Heart Disease | Chest Pain, Blood Pressure, Cholestrol, Max Heart Rate |

The feature selection is carefully done under the supervision of a medical science student.

## Future Prospects

- Addition of more disease prediction sections to cover more segments of medical domain
- Inclusion of a NLP chatbot for users to get advice regarding their diet and nutrition chart 
- Addition of a quiz section which will take inputs about the common diseases covered in the application and mark them as wrong and right to give users a detailed info regarding their disease

## UI Of The Web Application

### 2. Diabetes Prediction Section
<pre>
<img src="https://user-images.githubusercontent.com/78029145/158956887-0b407b26-1971-4957-af43-a15bfc173f50.png" width="1000"> <img src="https://user-images.githubusercontent.com/78029145/158956941-cac3a5c6-314d-46c0-87dc-96082dd328c0.png" width="1000">
</pre>

### 3. Covid-19 Prediction Section
<pre>
<img src="https://user-images.githubusercontent.com/78029145/158957322-5e76792c-201e-4743-8a74-2b2c736d3b40.png" width="1010"> <img src="https://user-images.githubusercontent.com/78029145/158957381-87c25f0b-3559-40d8-b911-b6f6b5fc4a50.png" width="1010"
</pre>

### 4. Heart Disease Prediction Section
<pre>
<img src="https://user-images.githubusercontent.com/78029145/158957765-d229878e-c2b7-45fb-9006-2bd05082b953.png" width="1010"> <img src="https://user-images.githubusercontent.com/78029145/158957853-bdc7aafd-3975-4825-bc31-f4c407e69542.png" width="1010">
</pre>
