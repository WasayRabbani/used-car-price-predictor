import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model pipeline
pipe = joblib.load('car_price_prediction.pkl')

st.set_page_config(page_title="Used Car Price Predictor", layout="wide")
st.title("🚗 Used Car Price Predictor")
st.markdown("Enter car details to predict its price. The app shows an estimated price range based on model performance (MAPE ~22%).")

# Create 2 columns for inputs
col1, col2 = st.columns(2)

with st.form("car_form"):
    with col1:
        brand = st.selectbox("Brand", ['Toyota', 'Honda', 'Ford', 'BMW', 'Rivian', 'Others'])
        fuel_type = st.selectbox("Fuel Type", ['Gasoline', 'Diesel', 'Electric', 'Hybrid', 'Others'])
        transmission = st.selectbox("Transmission", ['Automatic', 'Manual'])
        ext_col = st.selectbox("Exterior Color", ['White', 'Black', 'Silver', 'Red', 'Others'])
        int_col = st.selectbox("Interior Color", ['Black', 'Beige', 'Gray', 'Others'])
    
    with col2:
        milage = st.number_input("Milage (in miles)", min_value=0, step=1000)
        car_age = st.number_input("Car Age (years)", min_value=0, step=1)
        engine_HP = st.number_input("Engine Horsepower", min_value=0, step=10)
        displacement = st.number_input("Displacement (L)", min_value=0.0, step=0.1)
        accident = st.selectbox("Accident History", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
        is_Turbo = st.selectbox("Turbo Engine", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")

    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Prepare input dataframe
    input_df = pd.DataFrame({
        'brand': [brand],
        'fuel_type': [fuel_type],
        'transmission': [transmission],
        'ext_col': [ext_col],
        'int_col': [int_col],
        'milage': [milage],
        'car_age': [car_age],
        'engine_HP': [engine_HP],
        'displacement': [displacement],
        'accident': [accident],
        'is_Turbo': [is_Turbo]
    })
    
    # Make prediction (log price)
    y_pred_log = pipe.predict(input_df)
    predicted_price = np.expm1(y_pred_log)[0]
    
    # Add confidence range (based on MAPE ~22%)
    lower_bound = predicted_price * (1 - 0.22)
    upper_bound = predicted_price * (1 + 0.22)
    
    st.success(f"Predicted Price: ${predicted_price:,.0f}")
    st.info(f"Estimated Range: ${lower_bound:,.0f} - ${upper_bound:,.0f}")
