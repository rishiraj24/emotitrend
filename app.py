
import streamlit as st
from sentiments import analyse_sentiment
from matplotlib import pyplot as plt
from wordcloud import WordCloud

mood_to_music = {
    "Happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "Sad": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
    "Angry": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
    "Neutral": "https://open.spotify.com/playlist/37i9dQZF1DX3sCT1ItXgWZ"
}

st.title("🎵 EmotiTrend – Mood-Based Music Recommender")

user_input = st.text_area("Enter your recent thoughts or paste your tweet:")

if st.button("Analyze & Recommend"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        mood = analyse_sentiment(user_input)
        st.subheader(f"Detected Mood: {mood}")
        st.markdown(f"🎧 [Click here for your playlist]({mood_to_music[mood]})")

        # Bonus: word cloud
        st.subheader("🧠 Word Cloud of Your Text")
        wc = WordCloud(background_color="white", width=600, height=300).generate(user_input)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
