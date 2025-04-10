import streamlit as st
from modules.voice_input import get_voice_input
from modules.music_recommender import recommend_playlist
from modules.model_predictor import predict_emotion
import streamlit_lottie as st_lottie
import requests

st.set_page_config(page_title="EmotiTrend", page_icon="🎧", layout="centered")

# Function to load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

# Load Lottie
lottie_music = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_touohxv0.json")  # music animation

# Background gradient styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f6f9fc, #e4ecf5);
    }
    </style>
""", unsafe_allow_html=True)

# Fancy Header
st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>🎧 EmotiTrend</h1>
    <h4 style='text-align: center; color: gray;'>Your Mood, Your Music 🎶</h4>
    <br>
""", unsafe_allow_html=True)

# Lottie animation
if lottie_music:
    st_lottie.st_lottie(lottie_music, height=200, speed=1)

# Input mode
input_mode = st.radio("🛠️ Choose input mode:", ["📝 Text", "🎙️ Voice"], horizontal=True)
user_input = ""

# Input Collection
if input_mode == "📝 Text":
    user_input = st.text_area("🧠 Describe how you're feeling today:", placeholder="e.g., I'm feeling energetic and ready to conquer the world!")
elif input_mode == "🎙️ Voice":
    st.info("Click the button and start speaking...")
    if st.button("🔴 Record Mood"):
        user_input = get_voice_input()

# Mood detection and playlist
if user_input:
    with st.spinner("Analyzing your mood..."):
        mood = predict_emotion(user_input)

    # Mood color + emoji map
    mood_styles = {
        "happy": {"color": "#FFD700", "emoji": "😄"},
        "sad": {"color": "#6495ED", "emoji": "😢"},
        "angry": {"color": "#FF6347", "emoji": "😠"},
        "neutral": {"color": "#D3D3D3", "emoji": "😐"}
    }
    mood_data = mood_styles.get(mood, {"color": "#D3D3D3", "emoji": "🤔"})

    st.markdown(f"""
        <div style='text-align: center; padding: 15px; background-color: {mood_data["color"]}; 
        border-radius: 15px; margin-top: 20px; box-shadow: 0px 0px 10px #ccc;'>
            <h2>{mood_data["emoji"]} Detected Mood: <b>{mood.upper()}</b></h2>
        </div>
    """, unsafe_allow_html=True)

    playlist_url = recommend_playlist(mood)
    st.markdown("<br><h4>🔗 Your Personalized Playlist:</h4>", unsafe_allow_html=True)
    st.markdown(f"[🎵 Click here to enjoy your {mood} playlist]({playlist_url})", unsafe_allow_html=True)

    st.markdown("<br><hr><p style='text-align: center; color: gray;'>🎧 Powered by EmotiTrend · Hybrid Sentiment AI</p>", unsafe_allow_html=True)
