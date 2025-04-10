import pickle
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

# Load ML model and vectorizer (only if files exist)
model_path = os.path.join("ml_model", "model.pkl")
vectorizer_path = os.path.join("ml_model", "vectorizer.pkl")

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    ml_available = True
else:
    ml_available = False

# --- Hybrid VADER + TextBlob ---
def analyze_sentiment(text):
    vader_analyzer = SentimentIntensityAnalyzer()
    vader_score = vader_analyzer.polarity_scores(text)["compound"]
    blob_score = TextBlob(text).sentiment.polarity

    # Weighted average (can tune these weights)
    final_score = (0.7 * vader_score + 0.3 * blob_score)

    if final_score > 0.5:
        return "happy"
    elif final_score > 0.1:
        return "neutral"
    elif final_score < -0.5:
        return "angry"
    elif final_score < -0.1:
        return "sad"
    else:
        return "neutral"

# --- ML Classifier-based Sentiment (if available) ---
def analyze_sentiment_ml(text):
    if not ml_available:
        return "neutral"
    
    text = text.lower()
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    return "happy" if prediction == 1 else "sad"
