from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('trained_model_compatible.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return "Phishing Website Detection Model API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_features = data['input']
    prediction = model.predict([input_features])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=False)


