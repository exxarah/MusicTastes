import json

import spotipy
import os
from flask import render_template, redirect, url_for, request, session

from . import general_bp
from musictastes import app, spotipy_helpers


@general_bp.route('/')
def index():
    cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=app.config['SPOTIFY_CACHE'])
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        client_id=app.config['SPOTIFY_CLIENT_ID'],
        client_secret = app.config['SPOTIFY_CLIENT_SECRET'],
        redirect_uri = app.config['SPOTIFY_REDIRECT_URI'],
        scope=[
            'user-read-recently-played',    # Last 50 songs
            'user-library-read',            # Read Saved Tracks/Albums
            'user-read-email',              # Read User profile
        ],
        cache_handler=cache_handler,
        show_dialog=True
    )

    if request.args.get("code"):
        # Step 3: Redirected from spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect(url_for('general_bp.index'))

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 2: Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return render_template('index.html', auth_url=auth_url)

    # Step 4: Signed in, display data
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    print(f'Hi {spotify.me()["display_name"]}')

    return redirect(url_for('general_bp.vis_page'))


@general_bp.route('/vis/')
def vis_page():
    spotify = spotipy_helpers.get_spotify()
    songs = spotipy_helpers.get_recently_played()
    songs['items'] = sorted(songs['items'], key=lambda d: d['track']['album']['release_date'])
    songsJson = {}
    for item in songs['items']:
        songsJson[item["track"]["id"]] = json.JSONEncoder().encode(item)

    return render_template(
        'vis.html',
        logged_in=True,
        username=spotify.me()["display_name"],
        profile_pic=spotify.me()["images"][0]["url"],
        songs=songs,
        songsJson=songsJson,
    )


@general_bp.route('/logout/')
def logout():
    try:
        # Remove the cache file, so a new user can authorise
        os.remove(app.config['SPOTIFY_CACHE'])
        session.clear()
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    return redirect(url_for('general_bp.index'))
