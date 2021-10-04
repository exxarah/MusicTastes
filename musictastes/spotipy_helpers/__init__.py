import os
import json
from flask import redirect

from musictastes import app

import spotipy


def get_spotify():
    cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=app.config['SPOTIFY_CACHE'])
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        client_id=app.config['SPOTIFY_CLIENT_ID'],
        client_secret = app.config['SPOTIFY_CLIENT_SECRET'],
        redirect_uri = app.config['SPOTIFY_REDIRECT_URI'],
        scope=[
            'user-read-recently-played',    # Last 50 songs
            'user-library-read',            # Read Saved Tracks/Albums
        ],
        cache_handler=cache_handler,
        show_dialog=True
    )
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')

    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return spotify


def get_recently_played(spotify=get_spotify()):
    data = spotify.current_user_recently_played()
    return data


def fake_recently_played():
    result = ""
    with open(
            os.path.join(os.path.dirname(__file__),'..\\static\\data\\recently_played.txt'),
            'r',
            encoding='utf-8'
    ) as f:
        result = f.read()
    return result


def get_saved_tracks(spotify=get_spotify()):
    result = []
    offset = 0
    increment = 20
    while True:
        result.append(spotify.current_user_saved_tracks(offset=offset, limit=increment))
        if not result[-1]["next"]:
            break
        offset += increment
    return {'saved': result}


def fake_saved_tracks():
    result = ""
    with open(
            os.path.join(os.path.dirname(__file__), '..\\static\\data\\saved_tracks.txt'),
            'r',
            encoding='utf-8'
    ) as f:
        result = f.read()
    return result


def get_current_user(spotify=get_spotify()):
    return spotify.current_user()


def fake_current_user():
    result = ""
    with open(
            os.path.join(os.path.dirname(__file__), '..\\static\\data\\user_profile.txt'),
            'r',
            encoding='utf-8'
    ) as f:
        result = f.read()
    return result
