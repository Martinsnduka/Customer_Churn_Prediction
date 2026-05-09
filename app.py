# Gender --> 1 is female, 0 is male
# Churn --> 1 is Yes, 0 is No
# TechSupport --> 1 is Yes, 0 is No
# ContractType --> 0.0 is Month-to-Month, 1.0 is One-Year,2.0 is Two-Year
# Churn --> 1 is Yes, 0 is No
# Model is exported as model.pkl
# Order of X -->'Age', 'Gender', 'Tenure', 'MonthlyCharges', 'ContractType','TechSupport
# 


import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button")

st.divider()

Age = st.number_input("Age",min_value=10,max_value=100,value=30)

Tenure = st.number_input("Tenure", min_value=0,max_value=130,value=10)

MonthlyCharges = st.number_input("Monthly charges",min_value=30,max_value=150)

Gender = st.selectbox( "Gender",["Male", "Female"])

ContractType = st.selectbox("Contract Type",["Month-to-Month", "One-Year", "Two-Year"])

TechSupport = st.selectbox("Tech Support",["Yes", "No"])

st.divider()

PredictButton = st.button("Predict")

if PredictButton:

    Gender_selected = 1 if Gender == "Female" else 0

    ContractType_selected = (
        0.0 if ContractType == "Month-to-Month"
        else 1.0 if ContractType == "One-Year"
        else 2.0
    )

    TechSupport_selected = 1 if TechSupport == "Yes" else 0

    X = [ Age,Gender_selected,Tenure,MonthlyCharges,ContractType_selected,TechSupport_selected ]
    X1 = np.array(X)
    X_array = scaler.transform([X1])

    Prediction = model.predict(X_array)[0]
    Predicted = (
        "customer will churn"
        if Prediction == 1
        else "customer will not churn"
    )

    st.write(f"Predicted: {Predicted}")

else:
    st.write("Please enter the value and use the predict button")





