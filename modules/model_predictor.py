import joblib
import os

# Load model + vectorizer + labels
model = joblib.load("ml_model/emotion_model.pkl")
vectorizer = joblib.load("ml_model/vectorizer.pkl")
label_map = joblib.load("ml_model/label_map.pkl")

def predict_emotion(text):
    features = vectorizer.transform([text])
    pred_label = model.predict(features)[0]
    return label_map[pred_label]
