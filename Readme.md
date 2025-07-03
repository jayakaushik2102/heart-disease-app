Heart Disease Prediction App
A simple and interactive Streamlit web application that predicts the risk of heart disease based on patient input data. 
The model uses a trained logistic regression (or any other ML) model built with scikit-learn and provides instant results through a user-friendly interface.

Features
- Predicts heart disease risk (High or Low)
- Clean, interactive UI built with Streamlit
- Uses a trained Machine Learning model
- Deployed online for public use
- Accepts real patient inputs

Technologies Used
- Python
- Scikit-learn
- Streamlit
- Joblib (for model serialization)
- NumPy

Files Included
- heart_app.py → Main Streamlit app
- scaler.pkl → Preprocessing scaler
- heart_disease_model.pkl → Trained ML model
- requirements.txt → App dependencies

Try it Online
You can try the app directly on Streamlit Cloud:
Live Demo
https://heart-disease-app-2h5vaetdg6ehwdnwdnyzwu.streamlit.app/

Model Inputs
- Age
- Sex (0 = Female, 1 = Male)
- Chest Pain Type (0–3)
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar (0 or 1)
- Max Heart Rate Achieved
- Exercise Induced Angina
- Oldpeak
- Slope of ST Segment
- Number of Major Vessels (0–3)
- Thalassemia (1–3)

Sample Input Example

- Age: 52  
- Sex: 1  
- Chest Pain Type: 2  
- Resting BP: 130  
- Cholesterol: 250  
- Fasting Sugar: 0  
- Max Heart Rate: 150  
- Exang: 0

heart-disease-prediction/
├── heart_app.py
├── scaler.pkl
├── heart_disease_model.pkl
├── requirements.txt
└── README.md

About Me

I'm Jaya Kaushik, an M.Tech student passionate about machine learning and biotech applications.  
Connect with me on :
likdien: www.linkedin.com/in/jaya-kaushik-b51978237
github:  https://github.com/jayakaushik2102
                   



