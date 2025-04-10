import speech_recognition as sr
import streamlit as st

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now 🎙️")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand your speech.")
        except sr.RequestError:
            st.error("Error accessing Google Speech API.")
    return ""
