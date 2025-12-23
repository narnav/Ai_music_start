from flask import Flask, jsonify,request
from flask_cors import CORS
import csv
# imports for AI
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
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


@app.route("/learn", methods=["POST"])
def learn():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    try:
        age = int(data.get("age"))
        gender = int(data.get("gender"))
        genre = data.get("genre")

        ############################### The real learn
        music_file='music.csv'

        # loading data
        music_dt  =pd.read_csv(music_file)

        # prepare 2 groups (features, output)
        X=music_dt.drop(columns=['genre']) # sample features (age,gender) -X
        Y=music_dt['genre'] # sample output - Y -genre

        model = DecisionTreeClassifier()
        model.fit(X,Y)
        joblib.dump(model, 'our_pridction.joblib') #binary file
        ###############################END  The real learn

        if not genre:
            return jsonify({"error": "Genre is required for learning"}), 400

        # Append new row to CSV
        with open("music.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([age, gender, genre])

        return jsonify({
            "status": "success",
            "message": "Data added for learning",
            "age": age,
            "gender": gender,
            "genre": genre
        }), 200

    except ValueError:
        return jsonify({"error": "Invalid age or gender"}), 400    