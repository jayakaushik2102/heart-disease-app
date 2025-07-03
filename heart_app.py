import streamlit as st
import numpy as np
import joblib
import traceback
scaler = joblib.load(r"C:\Users\Shivam Kaushik\Desktop\Heart Disease Project\Outputs\scaler.pkl")
model = joblib.load(r"C:\Users\Shivam Kaushik\Desktop\Heart Disease Project\Outputs\heart_disease_model.pkl")
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.markdown("""
<style>
h1 {
    color: #FF4B4B;
    text-align: center;
}
.stButton>button {
    background-color: #FF4B4B;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1> Heart Disease Prediction </h1>", unsafe_allow_html=True)
st.sidebar.header("Enter Patient Details")
age = st.number_input("Age", 1, 120, 45)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG (0 = Normal, 1 = Abnormal, 2 = LVH)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate", 60, 220)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of ST segment", [0, 1, 2])
ca = st.selectbox("Number of major vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed defect, 3 = Reversible defect)", [1, 2, 3])
if st.button("Predict"):
   st.write("Predict button clicked!") 
   try:
     input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, 0, 0]])
     input_scaled = scaler.transform(input_data)
     prediction = model.predict(input_scaled)

     if prediction[0] == 1:
            st.error("High risk of heart disease")
     else:
            st.success("Low risk of heart disease")

   except Exception as e:
        st.error("Error occurred while predicting:")
        st.code(traceback.format_exc())

