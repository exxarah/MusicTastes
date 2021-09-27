import spotipy
from flask import render_template, redirect, url_for, request

from . import general_bp
from musictastes import app, spotipy_helpers


@general_bp.route('/')
def index():
    cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=app.config['SPOTIFY_CACHE'])
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        scope=[
            'user-read-recently-played',    # Last 50 songs
            'user-library-read',            # Read Saved Tracks/Albums
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
    cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=app.config['SPOTIFY_CACHE'])
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')

    spotify = spotipy.Spotify(auth_manager=auth_manager)
    # print(spotipy_helpers.get_recently_played(spotify))
    # print(spotipy_helpers.fake_recently_played(spotify))
    # print(spotipy_helpers.get_saved_tracks(spotify))
    # print(spotipy_helpers.fake_saved_tracks(spotify))
    # print(spotipy_helpers.get_current_user(spotify))
    # print(spotipy_helpers.fake_current_user(spotify))

    return render_template('vis.html')
