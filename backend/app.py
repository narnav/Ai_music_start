from flask import Flask, jsonify,request
from flask_cors import CORS

# imports for AI
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import joblib

app = Flask(__name__)
CORS(app)  # enables CORS for all routes

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server is running"})

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    model = joblib.load("our_pridction.joblib")

    # Convert to correct types
    gender = int(data.get("gender"))
    age = int(data.get("age"))

    if age < 0:
        return jsonify({"error": "Age must be positive"}), 400

    prediction = model.predict([[age, gender]])[0]  # take first value

    return jsonify({
        "status": "success",
        "genre": prediction,
        "gender": gender,
        "age": age
    }), 200
