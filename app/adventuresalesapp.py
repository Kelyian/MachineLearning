import streamlit as st
import joblib

mult_model = joblib.load('adventure_sales_model.pkl')
st.title("Adventure Sales Prediction app")

#user input 
tv = st.slider('TV Budget',0,300)
radio = st.slider("Radio Budget",0,50)
news = st.slider("News Budget",0,100)

prediction = mult_model.predict([[tv, radio, news]])
st.write(f"Predicted Sales: {prediction[0]}")