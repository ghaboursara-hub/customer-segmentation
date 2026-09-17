import streamlit as st
import numpy as np
import joblib

# Load Model & Scaler
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

# UI Design
st.title("📊 Customer Segmentation System")
st.write("Enter RFM values to predict customer segment:")

recency = st.number_input("Recency (Days since last purchase):", min_value=1, max_value=365, value=30)
frequency = st.number_input("Frequency (Total orders count):", min_value=1, max_value=200, value=5)
monetary = st.number_input("Monetary Value (Total spend in USD $):", min_value=1.0, max_value=100000.0, value=500.0)

if st.button("🔮 Predict Customer Segment"):
    input_data = np.array([[recency, frequency, monetary]])
    scaled_data = scaler.transform(input_data)
    cluster = kmeans.predict(scaled_data)[0]

    segments = {
        0: "Champions 🏆",
        1: "At-Risk Customers ⚠️",
        2: "New / Potential Customers 🚀"
    }
    st.success(f"Predicted Segment: **{segments.get(cluster, cluster)}**")