from config.mood_playlists import mood_to_playlist

def recommend_playlist(mood):
    return mood_to_playlist.get(mood, mood_to_playlist["neutral"])
