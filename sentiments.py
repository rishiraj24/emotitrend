from transformers import pipeline

# One-time setup
sentiment_pipeline = pipeline("sentiment-analysis")

def analyse_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE' and score >= 0.85:
        return "Happy"
    elif label == 'NEGATIVE' and score >= 0.85:
        return "Sad"
    else:
        return "Neutral"
