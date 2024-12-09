import streamlit as st
import pandas as pd
import base64
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
# # Menambahkan Logo dan Judul di Tengah
# st.image("C:/Users/ACER/Downloads/temp.png", width=300)

### gif from local file
file_ = open("C:/Users/ACER/Downloads/momoi.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
#st.title("Aplikasi Prediksi Diabetes")
st.markdown("<h1 style='text-align: center;'>Aplikasi Prediksi Diabetes</h1>", unsafe_allow_html=True)


# Sidebar Menu dengan Ikon
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Menu", [
    "📁 Unggah Data",
    "📊 Analisis Data",
    "📈 Evaluasi Model",
    "🔮 Prediksi",
    "🎨 Setting Tema"
])

# Fungsi untuk mengunggah file
@st.cache_data
def load_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)

# Fungsi preprocessing data
def preprocess_data(data, selected_columns, label_column, fill_method="mean"):
    X = data[selected_columns].drop(columns=[label_column])
    y = data[label_column]
    if fill_method == "mean":
        X.fillna(X.mean(), inplace=True)
    elif fill_method == "median":
        X.fillna(X.median(), inplace=True)
    elif fill_method == "zero":
        X.fillna(0, inplace=True)

    # Normalisasi
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return pd.DataFrame (X_scaled, columns=X.columns), y

# event
# def onClick

# Proses Unggah Data
if menu == "📁 Unggah Data":
    st.header("Unggah File Data")
    uploaded_file = st.file_uploader("Pilih file CSV atau Excel", type=["csv", "xlsx"])
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.dataframe(data)
        st.session_state['data'] = data

#Analisis Data
elif menu == "📊 Analisis Data" :
    st.header("Analisis Data")
    if 'data' in st.session_state:
        data = st.session_state['data']
        st.write("**Statistik Deskriptif:**")
        st.write(data.describe())
    
        #Menampilkan data kosong
        st.write("**Jumlah Data Kosong di Setiap Kolom:**")
        st.write(data.isnull().sum())

        #Memilih atribut untuk analisis
        st.write("**Pilih Atribut yang Akan Digunakan:**")
        selected_columns = st.multiselect("Pilih kolom:", options=data.columns.tolist(), default=data.columns.tolist())

        #Memilih kolom label
        label_column = st.selectbox("Pilih Kolom Label (Target):", options=selected_columns)

        if len(selected_columns) < 2:
            st.warning("Pilih minimal dua kolom (termasuk target).")
        else:
            # Opsi preprocessing
            fill_method = st.selectbox("Pilih metode untuk menangani data kosong:", ["mean", "median","zero"])
            if st.button("Lakukan Preprocessing"):
                X, y = preprocess_data(data, selected_columns, label_column, fill_method=fill_method)
                st.session_state['processed_data'] = (X, y)
                st.session_state['selected_columns'] = selected_columns
                st.session_state['label_column'] = label_column
                st.success("Preprocessing selesai!")
    else:
        st.warning("Unggah data terlebih dahulu pada menu 'Unggah Data'")

# Evaluasi Model
elif menu == "📈 Evaluasi Model":
    st.header("Evaluasi Model")
    if 'processed_data' in st.session_state:
        X, y = st.session_state['processed_data']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        #Membuat model Random Forest
        model = RandomForestClassifier (random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        #Menampilkan metrik
        st.write("**Confusion Matrix:**")
        st.write(confusion_matrix(y_test, y_pred))
        st.write("**Classification Report:**")
        st.text(classification_report(y_test, y_pred))
        st.write("**Accuracy:**", accuracy_score (y_test, y_pred))
    else:
        st.warning("Lakukan preprocessing data terlebih dahulu pada menu 'Analisis Data'.")

# Prediksi
elif menu == "🔮 Prediksi":
    st.header("Prediksi")
    if 'processed_data' in st.session_state:
        X, y = st.session_state['processed_data']
        selected_columns = st.session_state['selected_columns']
        label_column = st.session_state['label_column']
        model = RandomForestClassifier (random_state=42)
        model.fit(X, y)
    
        # Validasi input sesuai dataset
        st.write("**Masukkan data untuk prediksi:**")
        input_values = []
        valid_input = True
        for column in selected_columns:
            if column != label_column:
                value = st.number_input(f"Masukkan nilai untuk {column}:", value=0.0)
                input_values.append(value)
                if len(input_values) != X.shape[1]:
                    valid_input = False
                    st.error("Jumlah nilai input tidak sesuai dengan jumlah fitur dalam dataset.")

        #Tombol Prediksi
        if st.button("Prediksi") and valid_input:
            try:
                prediction = model.predict([input_values])
                #Menampilkan hasil prediksi sebagai label
                result = "Diabetes" if prediction [0] == 1 else "Tidak Diabetes"
                st.success(f"**Hasil Prediksi:** (result)")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Lakukan preprocessing data terlebih dahulu pada menu 'Analisis Data'.")

#Ubah Warna Tema
elif menu == "🎨 Setting Tema":
    st.header("Ubah Warna Tema")
    st.write("Pilih warna utama aplikasi:")
    primary_color = st.color_picker("Pilih warna utama:", "#FF4B4B")
    background_color = st.color_picker("Pilih warna latar belakang:", "#F0F2F6")
    secondary_background_color = st.color_picker("Pilih warna latar belakang sekunder:", "#FFFFFF")
    text_color = st.color_picker("Pilih warna teks:", "#000000")
    
    if st.button("change"):
        configFile = open("C:/Users/ACER/.streamlit/config.toml", "w")
        configFile.write("[theme]\n")
        configFile.write(f"primaryColor=\"{primary_color}\"\n")
        configFile.write(f"backgroundColor=\"{background_color}\"\n")
        configFile.write(f"secondaryBackgroundColor=\"{secondary_background_color}\"\n")
        configFile.write(f"textColor=\"{text_color}\"\n")
        configFile.write(f"font=\"sans serif\"")
        configFile.close()
        st.warning("refresh aplikasi atau double click")