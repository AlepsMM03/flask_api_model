from flask import Blueprint, request, jsonify
import joblib
import numpy as np
import os

api_bp = Blueprint('api', __name__)
model_path = os.path.join('model', 'random_forest_model2.pkl')
model = joblib.load(model_path)

@api_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "✅ API de predicción de infarto activa"})

@api_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    expected_fields = ['Troponin', 'CK-MB', 'Age']
    if not all(field in data for field in expected_fields):
        return jsonify({"error": f"Faltan uno o más campos requeridos: {expected_fields}"}), 400

    features = np.array([
        data['Troponin'],
        data['CK-MB'],
        data['Age']
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0][1]

    diagnosis = "Positivo para infarto" if prediction == 1 else "Negativo para infarto"

    return jsonify({
        "prediction": int(prediction),
        "probability": float(proba),  # Aseguramos que sea float para JSON
        "diagnosis": diagnosis,
        "input": {
            "Troponin": data['Troponin'],
            "CK-MB": data['CK-MB'],
            "Age": data['Age']
        }
    })
