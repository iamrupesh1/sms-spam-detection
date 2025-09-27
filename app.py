import streamlit as st
import pickle
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "spam_model.pkl")

# Load model
with open(MODEL_PATH, "rb") as f:
    vectorizer, model = pickle.load(f)

# App UI
st.set_page_config(page_title="📩 SMS Spam Detection", page_icon="📩", layout="centered")
st.title("📩 SMS Spam Detection")
st.write("Enter a message below and click Predict to check if it is Spam or Not Spam.")

# Input box
user_input = st.text_area("Type your message here:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        input_vect = vectorizer.transform([user_input])
        prediction = model.predict(input_vect)[0]
        prediction_proba = model.predict_proba(input_vect).max()  # Show confidence
        st.success(f"Prediction: **{prediction}**")
        st.info(f"Confidence: {prediction_proba*100:.2f}%")
