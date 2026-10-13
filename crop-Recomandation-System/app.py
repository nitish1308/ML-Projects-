"""
Crop Recommendation App
Run with:  streamlit run app.py
Keep 'crop_recommendation_model.pkl' in the same folder as this file.
"""
import numpy as np
import pandas as pd
import joblib
import streamlit as st

st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="centered")


# ---------- Load the saved model bundle ----------
@st.cache_resource
def load_bundle():
    return joblib.load("crop_recommendation_model.pkl")


# ---------- Same feature engineering used in the notebook ----------
def add_features(data):
    data = data.copy()
    data["NPK_sum"] = data["N"] + data["P"] + data["K"]
    data["N_P_ratio"] = data["N"] / (data["P"] + 1)
    data["N_K_ratio"] = data["N"] / (data["K"] + 1)
    data["P_K_ratio"] = data["P"] / (data["K"] + 1)
    data["temp_humidity"] = data["temperature"] * data["humidity"] / 100
    data["ph_category"] = np.where(data["ph"] < 6.5, 0, np.where(data["ph"] <= 7.5, 1, 2))
    return data


def predict(bundle, values):
    row = pd.DataFrame([values], columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"])
    row = add_features(row)[bundle["features"]]
    scaled = bundle["scaler"].transform(row)
    model, le = bundle["model"], bundle["label_encoder"]

    crop = le.inverse_transform(model.predict(scaled))[0]

    top3 = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(scaled)[0]
        idx = np.argsort(proba)[::-1][:3]
        top3 = [(le.inverse_transform([model.classes_[i]])[0], proba[i] * 100) for i in idx]
    return crop, top3


# ---------- UI ----------
bundle = load_bundle()

st.title("🌾 Crop Recommendation System")
st.caption(f"Model: **{bundle['model_name']}**  |  Test accuracy: **{bundle['accuracy']*100:.2f}%**")
st.write("Enter your soil and weather values to get the best crop to grow.")

st.subheader("🧪 Soil Nutrients")
c1, c2, c3 = st.columns(3)
N = c1.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=90.0, step=1.0)
P = c2.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=42.0, step=1.0)
K = c3.number_input("Potassium (K)", min_value=0.0, max_value=250.0, value=43.0, step=1.0)

st.subheader("🌦️ Weather & Soil Conditions")
c4, c5 = st.columns(2)
temperature = c4.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=20.9, step=0.1)
humidity = c5.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=82.0, step=0.1)
c6, c7 = st.columns(2)
ph = c6.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
rainfall = c7.number_input("Rainfall (mm)", min_value=0.0, max_value=400.0, value=202.9, step=0.1)

if st.button("🌱 Recommend Crop", use_container_width=True):
    crop, top3 = predict(bundle, [N, P, K, temperature, humidity, ph, rainfall])
    st.success(f"### ✅ Recommended crop: **{crop.upper()}**")

    if top3:
        st.write("**Top 3 suggestions:**")
        for name, conf in top3:
            st.progress(min(int(conf), 100), text=f"{name.title()} — {conf:.1f}%")
