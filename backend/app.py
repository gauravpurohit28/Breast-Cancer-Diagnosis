from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Incoming data:", data)

        features = data['features']
        print("Processed features:", features)

        prediction = model.predict([features])[0]
        result = "Malignant" if prediction == 0 else "Benign"
        return jsonify({'prediction': result})

    except Exception as e:
        print(" Error during prediction:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
