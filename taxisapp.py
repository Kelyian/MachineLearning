import streamlit as st
#importing the trained model
import joblib
regr = joblib.load('taxi_fare_model.pkl')

st.title("Taxi Fare Prediction App")
distance = st.number_input("Enter distance (miles):", min_value=0.0, step=0.1)
passengers = st.number_input("Enter number of passengers:", min_value=1, step=1)
if st.button("Predict Fare"):
    input_data = [[distance,passengers]]
    prediction = regr.predict(input_data)
    st.write(f"Estimated Fare: {prediction[0]:.2f}")