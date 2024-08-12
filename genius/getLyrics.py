from lyricsgenius import Genius
import os
from dotenv import load_dotenv

load_dotenv()
genius = Genius(os.getenv("token"))

def get_lyrics(title, artist):
    song = genius.search_song(f"{title}", f"{artist}").lyrics
    print(song)
    return genius.search_song(f"{title}", f"{artist}").lyrics
