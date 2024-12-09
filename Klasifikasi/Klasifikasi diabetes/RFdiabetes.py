import streamlit as st
import numpy as np
import joblib
#Muat model dan scaler
model = joblib.load("diabetes_model.sav")
scaler = joblib.load("scaler.sav")

#Fungsi prediksi
def predict_diabetes (input_data):
    #Normalisasi input menggunakan scaler
    input_data_scaled = scaler.transform(np.array(input_data).reshape(1, -1))
    prediction = model.predict(input_data_scaled)
    return prediction [0] # Mengembalikan hasil prediksi (0 atau 1)

# Streamlit UI
st.title("Sistem Informasi Prediksi Diabetes")
st.write("Masukkan data pasien untuk memprediksi diabetes.")

#Input fitur dari pengguna
pregnancies = st.number_input("Pregnancies", 0, 20, step=1)
glucose = st.number_input("Glucose", 0.0, 300.0, step=1.0)
blood_pressure = st.number_input("Blood Pressure", 0.0, 200.0, step=1.0)
skin_thickness = st.number_input("Skin Thickness", 0.0, 100.0, step=1.0)
insulin = st.number_input("Insulin", 0.0, 900.0, step=1.0)
bmi = st.number_input("BMI", 0.0, 70.0, step=0.1)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, step=0.01)
age = st.number_input("Age", 1, 120, step=1)

# Kumpulkan input ke dalam list
input_features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]

# Prediksi ketika tombol ditekan
if st.button("Predict"):
    result = predict_diabetes (input_features)
    if result == 1:
        st.error("Model memprediksi bahwa pasien terindikasi diabetes.")
    else:
        st.success("Model memprediksi bahwa pasien tidak terindikasi diabetes.")