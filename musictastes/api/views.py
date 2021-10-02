from . import api_bp
from musictastes import app, spotipy_helpers


@api_bp.route('/me/')
def get_me():
    return spotipy_helpers.get_current_user()


@api_bp.route('/played/')
def get_played():
    return spotipy_helpers.get_recently_played()


@api_bp.route('/saved/')
def get_saved():
    return spotipy_helpers.get_saved_tracks()
