import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open('finalmodel.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("📊 Sales Prediction App")
st.write("Predict **Sales** based on **TV and Radio advertising spend**.")

# --- Centered input fields ---
tv_input = st.number_input("TV Advertising ($)", min_value=0.0, value=100.0)
radio_input = st.number_input("Radio Advertising ($)", min_value=0.0, value=30.0)

# --- Predict button ---
if st.button("Predict Sales"):
    input_data = pd.DataFrame({'TV': [tv_input], 'Radio': [radio_input]})
    predicted_sales = model.predict(input_data)[0]
    st.success(f"Predicted Sales: **{predicted_sales:.2f} units**")
