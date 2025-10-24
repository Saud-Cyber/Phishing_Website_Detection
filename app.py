import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open('trained_model_compatible.pkl', 'rb') as file:
    model = pickle.load(file)

# Page title
st.title("Phishing Website Detection Web App")

st.write("Enter the features below to check if a website is phishing or legitimate.")

# Example: Suppose your model expects 6 features.
# Adjust the labels and input types as needed based on your model's requirements.
feature_names = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6']

input_features = []
for name in feature_names:
    val = st.number_input(f"Enter {name}:", value=0.0)
    input_features.append(val)

if st.button("Predict"):
    # Reshape for model: 2D array required by scikit-learn models
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    
    if prediction == 1:
        st.success("Phishing website detected!")
    else:
        st.info("Legitimate website detected.")
