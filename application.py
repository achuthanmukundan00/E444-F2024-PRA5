from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

application = Flask(__name__)


# Function to load the model and vectorizer
def load_model():
    global loaded_model, vectorizer
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)


# Load the model on application startup
load_model()


# Define a route to predict fake news
@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data
    print(f"Received request data: {data}")  # Debug: print received data

    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    print(f"Text to predict: {text}")  # Debug: print the text to be predicted

    transformed_text = vectorizer.transform([text])
    prediction = loaded_model.predict(transformed_text)[0]
    print(f"Prediction result: {prediction}")  # Debug: print prediction result

    # Return the prediction
    result = 'REAL' if prediction == 'REAL' else 'FAKE'
    return jsonify({'prediction': result})


# Main entry point for the application
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
