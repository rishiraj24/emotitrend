from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def analyze_sentiment(text):
    # VADER analysis
    vader_analyzer = SentimentIntensityAnalyzer()
    vader_score = vader_analyzer.polarity_scores(text)['compound']

    # TextBlob analysis
    blob_score = TextBlob(text).sentiment.polarity

    # Combine scores
    final_score = (vader_score + blob_score) / 2

    # Mood classification
    if final_score >= 0.35:
        return "Happy"
    elif final_score <= -0.35:
        return "Sad"
    elif -0.35 < final_score < 0.05:
        return "Neutral"
    else:
        return "Angry"

   
   
   
   
    # if final_score >= 0.5:
    #     return "Happy"
    # elif final_score <= -0.3:
    #     return "Sad"
    # elif -0.3 < final_score < 0.3:
    #     return "Neutral"
    # else:
    #     return "Angry"



















# from textblob import TextBlob

# def analyze_sentiment(text):
#     blob = TextBlob(text)
#     polarity = blob.sentiment.polarity

#     if polarity >= 0.5:
#         return "Happy"
#     elif polarity <= -0.3:
#         return "Sad"
#     elif -0.3 < polarity < 0.3:
#         return "Neutral"
#     else:
#         return "Angry"



# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# def analyze_sentiment(text):
#     analyzer = SentimentIntensityAnalyzer()
#     score = analyzer.polarity_scores(text)
#     compound = score['compound']
    
#     if compound >= 0.5:
#         return "Happy"
#     elif compound <= -0.5:
#         return "Sad"
#     elif -0.5 < compound < 0.5 and abs(score['neu']) < 0.8:
#         return "Angry"
#     else:
#         return "Neutral"
