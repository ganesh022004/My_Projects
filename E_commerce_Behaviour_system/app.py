import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

st.title("🛒 E-Commerce Purchase Predictor")
st.write("Fill in the user details to predict if they will make a purchase.")

# Input fields
age = st.slider("Age", 18, 70, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
device_type = st.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
time_on_site = st.number_input("Time on Site (minutes)", 0.0, 300.0, 10.0)
pages_viewed = st.number_input("Pages Viewed", 1, 100, 5)
previous_purchases = st.number_input("Previous Purchases", 0, 50, 2)
cart_items = st.number_input("Cart Items", 0, 20, 1)

# 👉 MISSING FEATURES ADD KIYE
discount_seen = st.selectbox("Discount Seen", ["No", "Yes"])
ad_clicked = st.selectbox("Ad Clicked", ["No", "Yes"])
returning_user = st.selectbox("Returning User", ["No", "Yes"])

avg_session_time = st.number_input("Avg Session Time (minutes)", 0.0, 120.0, 10.0)
bounce_rate = st.slider("Bounce Rate", 0.0, 100.0, 50.0)

# Encode inputs
gender_enc = 0 if gender == "Male" else 1
device_enc = {"Mobile": 0, "Desktop": 1, "Tablet": 2}[device_type]

discount_enc = 1 if discount_seen == "Yes" else 0
ad_enc = 1 if ad_clicked == "Yes" else 0
returning_enc = 1 if returning_user == "Yes" else 0

# Predict button
if st.button("Predict"):
    features = np.array([[age, gender_enc, device_enc, time_on_site,
                          pages_viewed, previous_purchases, cart_items,
                          discount_enc, ad_enc, returning_enc,
                          avg_session_time, bounce_rate]])
    
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.success("✅ This user is likely to PURCHASE!")
    else:
        st.warning("❌ This user is NOT likely to purchase.")