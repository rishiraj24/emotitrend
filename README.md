#  EmotiTrend – Mood-Based Music Recommender 🎧 
EmotiTrend is an AI-powered web app that detects your emotional state from the text you type (like journal entries or tweets), and recommends a Spotify playlist that matches your mood — happy, sad, angry, chill, etc. It's built using NLP sentiment analysis (VADER + TextBlob) and Streamlit.

________________________________________________________________________________________________________________________________________________________________________________________________________________

# Features
🧠 Emotion Detection using hybrid VADER + TextBlob sentiment scoring.

🎵 Spotify Playlist Recommendations based on mood.

💡 Minimal UI built with Streamlit.

💬 Enter your thoughts, get a vibe-matched playlist instantly.

________________________________________________________________________________________________________________________________________________________________________________________________________________

# Tech Stack
**Frontend:** Streamlit

**NLP Libraries:** VADER, TextBlob

**Language:** Python 3.13

**Other Tools:** Matplotlib (optional), Requests


________________________________________________________________________________________________________________________________________________________________________________________________________________

# How It Works
User types in their current thoughts or mood.

The app uses VADER and TextBlob to analyze the sentiment polarity.

It averages both models' scores for better mood detection.

**Based on the final sentiment:**

😊 Happy → Upbeat playlists

😢 Sad → Calm, healing music

😠 Angry → Intense rock/metal

😌 Neutral → Chill, lo-fi beats
