from shazam.getSong import get_song
# from shazam.recordAudio import record_audio
from genius.getInfo import get_info
from genius.getLyrics import get_lyrics

from flask import Flask, request, jsonify
from flask_cors import CORS


def song_lyrics():
    song_title_artist = get_song()
    title, artist = get_info(song_title_artist)
    return get_lyrics(title, artist)

song_lyrics()
