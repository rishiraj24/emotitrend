import streamlit as st
from modules.voice_input import get_voice_input
from modules.music_recommender import recommend_playlist
from modules.model_predictor import predict_emotion

st.set_page_config(page_title="EmotiTrend", page_icon="🎧")

st.title("🎧 EmotiTrend – Mood-Based Music Recommender")

input_mode = st.radio("Choose input mode:", ["Text", "Voice"])
user_input = ""

if input_mode == "Text":
    user_input = st.text_area("Describe how you're feeling today:")
elif input_mode == "Voice":
    if st.button("🎙️ Record Mood"):
        user_input = get_voice_input()

if user_input:
    mood = predict_emotion(user_input)
    st.subheader(f"🧠 Detected Mood: **{mood.upper()}**")

    playlist_url = recommend_playlist(mood)
    st.markdown(f"[🎵 Click here for your {mood} playlist]({playlist_url})", unsafe_allow_html=True)

