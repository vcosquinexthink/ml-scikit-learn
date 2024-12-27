from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.datasets import load_iris

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model (make sure the model.pkl file is in the same directory)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load Iris dataset to map predicted labels to flower names
iris = load_iris()

# Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        data = request.get_json()  # Expecting a JSON payload
        features = np.array(data['features']).reshape(1, -1)  # Reshape for a single prediction

        # Make prediction
        prediction = model.predict(features)
        predicted_class = iris.target_names[prediction][0]

        # Return prediction as a JSON response
        return jsonify({'predicted_class': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

