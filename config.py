"""Configuration for MusicTastes"""
import os

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Application Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, "musictastes")
STATIC_DIR = os.path.join(APP_DIR, "static")

# Define Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, 'musictastes.db')
SQLALCHEMY_BINDS = {}
DATABASE_CONNECT_OPTIONS = {}

# Auth Stuff
SECRET_KEY = 'L0L_PLZ_N0_HAX'
LOGIN_DISABLED = False
TESTING = False

# Spotify/OAuth Stuff
from config_secret import *
SPOTIFY_CACHE = '.spotifyoauthcache'
