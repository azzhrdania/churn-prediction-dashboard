import streamlit as st
import pandas as pd
import joblib
import os

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction Dashboard")
st.write(
    "Dashboard ini bertujuan untuk membantu pengambilan keputusan bisnis dengan "
    "menyediakan prediksi risiko churn pelanggan. Sistem ini memanfaatkan model "
    "machine learning yang dibangun dari data historis pelanggan untuk memberikan "
    "estimasi risiko serta wawasan terkait faktor-faktor yang memengaruhinya."
)

# ===============================
# LOAD MODEL
# ===============================
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "churn_pipeline.pkl")
pipeline = joblib.load(MODEL_PATH)

# ===============================
# FORM INPUT
# ===============================
with st.form("churn_form"):
    st.subheader("👤 Informasi Pelanggan")
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])

    st.subheader("🌐 Informasi Layanan")
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    st.subheader("💳 Kontrak & Pembayaran")
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    st.subheader("💰 Finansial & Durasi")
    tenure = st.number_input("Tenure (bulan)", min_value=0)
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0)

    submit = st.form_submit_button("🔮 Predict Churn")

# ===============================
# PREDICTION
# ===============================
if submit:
    input_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    input_df = pd.DataFrame([input_data])

    prediction = pipeline.predict(input_df)[0]
    probability = pipeline.predict_proba(input_df)[0][1]

    # ===============================
    # OUTPUT
    # ===============================
    st.divider()
    st.subheader("📊 Hasil Prediksi")

    churn_text = "YES ❌ (Berpotensi Churn)" if prediction == 1 else "NO ✅ (Tidak Churn)"
    st.success(f"Prediction: {churn_text}")

    st.metric("Probabilitas Churn", f"{probability*100:.2f}%")
    st.progress(probability)

    if probability < 0.3:
        st.success("🟢 Tingkat Risiko: LOW")
    elif probability < 0.6:
        st.warning("🟡 Tingkat Risiko: MEDIUM")
    else:
        st.error("🔴 Tingkat Risiko: HIGH")

    # ===============================
    # FAKTOR PENYEBAB
    # ===============================
    st.divider()
    st.subheader("🔍 Faktor Utama Penyebab Risiko Churn")

    if Contract == "Month-to-month":
        st.markdown("**Jenis Kontrak (Bulanan)**")
        st.progress(0.8)
        st.caption(
            "Pelanggan dengan kontrak bulanan memiliki tingkat komitmen yang lebih rendah "
            "sehingga lebih berisiko untuk berhenti berlangganan."
        )

    if tenure < 12:
        st.markdown("**Masa Berlangganan Pendek**")
        st.progress(0.7)
        st.caption(
            "Pelanggan dengan masa berlangganan singkat cenderung belum memiliki loyalitas "
            "yang kuat terhadap layanan."
        )

    if MonthlyCharges > 80:
        st.markdown("**Biaya Bulanan Tinggi**")
        st.progress(0.6)
        st.caption(
            "Biaya bulanan yang tinggi dapat meningkatkan ketidakpuasan pelanggan "
            "jika tidak sebanding dengan manfaat yang diterima."
        )

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.markdown(
    "© 2026 **Azzahra Dania Indriyani** | Customer Churn Prediction Dashboard"
)