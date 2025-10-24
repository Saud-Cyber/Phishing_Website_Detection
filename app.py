import streamlit as st
import pickle
import numpy as np
from urllib.parse import urlparse

# Example feature extraction function
def extract_features(url):
    parsed = urlparse(url)
    length = len(url)
    count_dots = url.count('.')
    has_https = 1 if url.startswith('https://') else 0
    domain_length = len(parsed.netloc)
    # Add more features here if your model requires them

    return [length, count_dots, has_https, domain_length]

# Load the pre-trained model
with open('trained_model_compatible.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app UI
st.title("Phishing Website Detection")

st.write("Enter a URL below to predict whether it is a phishing website or legitimate.")

url = st.text_input("Enter URL")

if st.button("Predict"):
    if not url:
        st.warning("Please enter a URL to proceed.")
    else:
        try:
            # Extract features from the URL
            features = extract_features(url)
            features_array = np.array(features).reshape(1, -1)

            # Predict using the loaded model
            prediction = model.predict(features_array)[0]

            # Display result
            if prediction == 1:
                st.error("Warning: This URL is predicted as a PHISHING website.")
            else:
                st.success("This URL is predicted as a LEGITIMATE website.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
