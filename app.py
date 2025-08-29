import streamlit as st
import numpy as np
import joblib   # 👈 use joblib instead of pickle
from pathlib import Path

# Load your trained model (make sure you have a saved model.joblib file)
model = joblib.load(Path("artifacts") / "model_trainer" / "model.joblib")


st.set_page_config(page_title="Wine Quality Prediction", page_icon="🍷", layout="centered")

# App Header
st.title("🍷 Wine Quality Prediction")
st.subheader("A Wine Quality Checking Web App")

st.markdown("Fill the details below to check the wine quality:")

# Form Inputs
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, format="%.2f")
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, format="%.2f")
citric_acid = st.number_input("Citric Acid", min_value=0.0, format="%.2f")
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, format="%.2f")
chlorides = st.number_input("Chlorides", min_value=0.0, format="%.4f")
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, format="%.2f")
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, format="%.2f")
density = st.number_input("Density", min_value=0.0, format="%.4f")
ph = st.number_input("pH", min_value=0.0, format="%.2f")
sulphates = st.number_input("Sulphates", min_value=0.0, format="%.2f")
alcohol = st.number_input("Alcohol", min_value=0.0, format="%.2f")

# Prediction Button
if st.button("Predict"):
    # Convert input to array
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                            chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                            ph, sulphates, alcohol]])

    prediction = model.predict(input_data)[0]

    st.success(f"✅ Predicted Wine Quality: **{prediction}**")
