import streamlit as st
import pandas as pd
import joblib
from src.config.config import load_config

st.set_page_config(page_title="Vehicle Price Predictor")

st.title("🚗 Vehicle Price Predictor")

# Load config and model
cfg = load_config()
model = joblib.load(cfg["paths"]["model_file"])

# Load dataset for dropdown options (adjust path)
df = pd.read_csv(cfg["paths"]["raw_data"])

# UI Inputs
year = st.number_input("Year", min_value=1990, max_value=2025, value=2018)
mileage = st.number_input("Mileage (in km)", min_value=0, value=30000)

# Dynamic Make Dropdown
make_options = sorted(df["make"].dropna().unique())
make = st.selectbox("Select Make", options=make_options)

# Filter Models based on selected Make
model_options = sorted(df[df["make"] == make]["model"].dropna().unique())
model_name = st.selectbox("Select Model", options=model_options)

# Predict Button
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "year": year,
        "mileage": mileage,
        "make": make,
        "model": model_name
    }])

    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Estimated Price: ₹{predicted_price:,.2f}")
