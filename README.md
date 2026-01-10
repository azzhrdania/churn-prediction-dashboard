# 📊 Customer Churn Prediction Dashboard

Customer Churn Prediction Dashboard merupakan aplikasi berbasis web yang
dikembangkan untuk membantu pengambilan keputusan bisnis dengan memprediksi
risiko pelanggan berhenti berlangganan (churn).

Aplikasi ini memanfaatkan model *machine learning* yang dilatih menggunakan
data pelanggan untuk menghasilkan prediksi churn, tingkat risiko, serta
penjelasan faktor-faktor utama yang memengaruhi risiko tersebut.

---

## 🎯 Tujuan Sistem
Dashboard ini bertujuan untuk:
- Memprediksi kemungkinan pelanggan melakukan churn
- Mengelompokkan tingkat risiko churn (Low, Medium, High)
- Menyajikan faktor utama penyebab risiko churn secara informatif
- Membantu pihak manajemen atau pengambil keputusan dalam menentukan strategi retensi pelanggan

Sistem ini dirancang agar dapat dipahami oleh pengguna non-teknis
melalui visualisasi dan penjelasan berbasis data.

---

## 🧠 Pendekatan yang Digunakan
- Model *machine learning* berbasis data historis pelanggan
- Prediksi probabilitas churn
- Interpretasi faktor risiko berdasarkan kontribusi fitur terhadap model
- Visualisasi risiko dan faktor utama dalam dashboard interaktif

---

## ⚙️ Teknologi yang Digunakan
- **Python**
- **Streamlit** (Dashboard)
- **Pandas** (Pengolahan data)
- **NumPy** (Komputasi numerik)
- **Scikit-learn** (Machine Learning)
- **Joblib** (Model serialization)

---

## 📁 Struktur Folder
```text
customer-churn-dashboard/
├── dashboard.py                 # File utama dashboard Streamlit
├── churn_pipeline.pkl           # Model machine learning terlatih
├── requirements.txt             # Daftar dependensi
└── README.md                    # Dokumentasi proyek
