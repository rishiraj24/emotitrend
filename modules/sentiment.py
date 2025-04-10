from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    vader_analyzer = SentimentIntensityAnalyzer()

    # VADER score
    vader_score = vader_analyzer.polarity_scores(text)["compound"]

    # TextBlob score
    blob_score = TextBlob(text).sentiment.polarity

    # Weighted average (more weight to VADER)
    final_score = (0.7 * vader_score + 0.3 * blob_score)

    # Classify mood based on weighted score
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
