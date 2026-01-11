# 📊 Customer Churn Prediction Dashboard
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-red)](https://streamlit.io/) [![Scikit-learn](https://img.shields.io/badge/Model-ML-green)](https://scikit-learn.org/stable/) [![Status](https://img.shields.io/badge/Status-Active-success)]()

> **End-to-End Machine Learning Project** untuk memprediksi risiko pelanggan berhenti berlangganan (*churn*) agar bisnis dapat mengambil keputusan yang lebih tepat dan proaktif dalam strategi retensi pelanggan.  

---

## 🎯 Tujuan Proyek
Proyek ini bertujuan untuk:  
- Membantu stakeholder bisnis (manajer, analis, decision maker) memahami risiko churn pelanggan  
- Menyediakan hasil prediksi yang **mudah dipahami oleh non-teknis**  
- Menjembatani hasil analisis data dengan **insight yang actionable**  
- Menjadi studi kasus penerapan **machine learning end-to-end** (analisis → model → dashboard → deployment)  

---

## 👥 Target Pengguna Dashboard
Dashboard ini ditujukan untuk:  
- **Manajer Bisnis / Customer Retention Team**  
- **Analis Data**  
- **Akademisi / Mahasiswa**  
- **Recruiter & Reviewer Portofolio**  

Dashboard **tidak ditujukan untuk user teknis ML**, melainkan untuk pengguna yang membutuhkan **ringkasan keputusan berbasis data**.  

---

## 🧠 Cara Kerja Sistem (High-Level)
1. Data pelanggan dimasukkan melalui form dashboard  
2. Data diproses menggunakan **pipeline machine learning** (preprocessing + model)  
3. Model menghasilkan:  
    - Prediksi churn (YES / NO)  
    - Probabilitas churn (0–100%)  
4. Probabilitas dikonversi menjadi **tingkat risiko**  
5. Dashboard menampilkan:  
    - Hasil prediksi  
    - Visualisasi risiko  
    - Penjelasan faktor utama penyebab churn  

---

## 📊 Evaluasi Model
Dalam project ini, kami membandingkan **dua algoritma** untuk memprediksi churn pelanggan: **Logistic Regression** dan **Random Forest**.  

| Model | Accuracy | Precision | Recall | F1-Score | Kelebihan |
|-------|---------|----------|--------|----------|-----------|
| Logistic Regression | 0.81 | 0.66 | 0.57 | 0.61 | Simpel, cepat, interpretasi mudah |
| Random Forest | 0.79 | 0.62 | 0.49 | 0.55 | Menangkap pola non-linear, sedikit lebih kompleks |

> **Keputusan Deployment:** Logistic Regression dipilih sebagai **algoritma utama** karena memberikan akurasi lebih tinggi pada dataset ini, interpretasi model lebih mudah, dan ringan untuk inferensi real-time.  

---

## 📈 Interpretasi Hasil Prediksi
### 🔹 Prediction
- **YES (Churn)** → Pelanggan berpotensi berhenti berlangganan  
- **NO (Not Churn)** → Pelanggan relatif stabil  

### 🔹 Churn Probability
Menunjukkan **kemungkinan pelanggan churn** berdasarkan pola data historis pelanggan serupa.  
Contoh: `0.72` → Artinya terdapat kemungkinan churn sebesar **72%**  

### 🔹 Risk Level
Tingkat risiko ditentukan berdasarkan threshold berikut:  

| Probability | Risk Level |
|------------|------------|
| < 0.30     | Low        |
| 0.30–0.59  | Medium     |
| ≥ 0.60     | High       |

> Threshold ini digunakan untuk **klasifikasi risiko bisnis**, bukan sebagai keputusan mutlak.  

---

## 🔍 Faktor Utama Penyebab Churn
Dashboard menampilkan **3 faktor dominan** yang berkontribusi terhadap risiko churn, berdasarkan **analisis pengaruh fitur pada model** dan **pola umum data pelanggan**:  

### 1️⃣ Jenis Kontrak (Month-to-month)
- Pelanggan dengan kontrak bulanan memiliki komitmen lebih rendah dan fleksibilitas tinggi → risiko churn lebih tinggi  

### 2️⃣ Masa Berlangganan (Tenure Rendah)
- Pelanggan baru masih dalam tahap eksplorasi layanan → loyalitas rendah → risiko churn meningkat  

### 3️⃣ Biaya Bulanan Tinggi (Monthly Charges)
- Biaya tinggi tanpa persepsi nilai sepadan → menurunkan kepuasan pelanggan → risiko churn meningkat  

> Faktor-faktor ini dipilih karena memiliki **pengaruh terbesar (nilai koefisien absolut tinggi)** terhadap prediksi churn pada model yang digunakan.  

---

## 📊 Visualisasi dalam Dashboard
Dashboard menyediakan:  
- Progress bar probabilitas churn  
- Indikator risk level (Low / Medium / High)  
- Visualisasi faktor risiko dengan penjelasan deskriptif  

Dirancang agar:  
- Mudah dipahami oleh non-teknis  
- Mendukung pengambilan keputusan cepat  

---

## 🧪 Teknologi yang Digunakan
- **Python**  
- **Pandas & NumPy**  
- **Scikit-learn**  
- **Joblib**  
- **Streamlit**  
- **Git & GitHub**  

---

## 🚀 Deployment
Dashboard ini dideploy menggunakan **Streamlit Community Cloud** dan memuat model `.pkl` secara langsung tanpa API eksternal.  

---

## ⚠️ Disclaimer

- Prediksi yang dihasilkan bersifat **pendukung keputusan**
- Model tidak menggantikan evaluasi bisnis atau kebijakan perusahaan
- Hasil prediksi bergantung pada kualitas dan pola data historis

---

## 👩‍💻 Author

**Azzahra Dania Indriyani**  
Customer Churn Prediction Dashboard  
© 2026

---

## 🔗 Repository

GitHub Repository:  
👉 https://github.com/azzhrdania/churn-prediction-dashboard
