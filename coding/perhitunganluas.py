import streamlit as st
from streamlit_option_menu import option_menu
#Judul aplikasi
st.title("Aplikasi Perhitungan Luas")
# Menu navigasi dengan streamlit_option_menu
menu = option_menu(
    menu_title="Menu Perhitungan", # Judul menu
    options=["Luas Persegi Panjang", "Luas Segitiga", "Luas Persegi"], # Pilihan menu
    icons=["bounding-box", "triangle", "square"], # Ikon untuk setiap pilihan
    menu_icon="calculator", # Ikon menu
    default_index=0, # Pilihan default
    orientation="horizontal"
)
# Orientasi menu (horizontal atau vertical)

# Perhitungan berdasarkan pilihan menu
if menu == "Luas Persegi Panjang":
    st.subheader("Menghitung Luas Persegi Panjang")
    panjang = st.number_input("Masukkan Panjang (dalam meter):", min_value=0.0, step=0.1)
    lebar = st.number_input("Masukkan Lebar (dalam meter):", min_value=0.0, step=0.1)
    if st.button("Hitung Luas"):
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang adalah {luas} meter persegi")
elif menu == "Luas Segitiga":
    st.subheader("Menghitung Luas Segitiga")
    alas = st.number_input("Masukkan Alas (dalam meter):", min_value=0.0, step=0.1)
    tinggi = st.number_input("Masukkan Tinggi (dalam meter):", min_value=0.0, step=0.1)
    if st.button("Hitung Luas"):
        luas = 0.5* alas * tinggi
        st.success(f"Luas Segitiga adalah {luas} meter persegi")
elif menu == "Luas Persegi":
    st.subheader("Menghitung Luas Persegi")
    sisi = st.number_input("Masukkan Panjang Sisi (dalam meter):", min_value=0.0, step=0.1)
    if st.button("Hitung Luas"):
        luas = sisi ** 2
        st.success(f"Luas Persegi adalah {luas} meter persegi")
        