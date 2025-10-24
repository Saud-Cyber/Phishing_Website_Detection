import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('trained_model_compatible.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Phishing Website Detection")

st.write("Enter a URL below to check if it is a phishing website or legitimate.")

# Input URL from user
input_url = st.text_input("Enter URL:", "")

if st.button("Predict"):
    if not input_url:
        st.warning("Please enter a URL to proceed.")
    else:
        # Depending on your model, you may need to extract or encode features from input_url
        # For example, here we assume the model accepts a feature vector extracted elsewhere
        # Replace the following line with your actual feature extraction from the URL
        # Example placeholder: input_features = extract_features_from_url(input_url)

        # For demonstration, let's pretend the URL is converted into a dummy numeric feature vector:
        # WARNING: Replace this with your actual feature extraction logic
        input_features = np.array([len(input_url), sum(ord(c) for c in input_url) % 100]).reshape(1, -1)

        try:
            prediction = model.predict(input_features)[0]

            if prediction == 1:
                st.error("Warning: This URL is predicted as a PHISHING website.")
            else:
                st.success("This URL is predicted as a LEGITIMATE website.")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
