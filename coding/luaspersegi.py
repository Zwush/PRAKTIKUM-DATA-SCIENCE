import streamlit as st
#Judul aplikasi
st.title("Aplikasi Penghitung Luas Persegi Panjang")
# Input panjang dan lebar (mendukung bilangan desimal)
panjang = st.slider("Masukkan Panjang (dalam satuan meter):", min_value=0.0, max_value=100.0,step=0.1)
lebar = st.slider("Masukkan Lebar (dalam satuan meter):", min_value=0.0, max_value=100.0,step=0.1)
# Tombol untuk menghitung
if st.button("Hitung Luas"):
    luas = panjang * lebar
    st.success(f"Luas Persegi Panjang adalah {luas} meter persegi")
else:
    st.write("Masukkan nilai panjang dan lebar, lalu tekan tombol 'Hitung Luas'.")