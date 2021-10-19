# MusicTastes

## Description

A webapp created for Massey University's 289.212 Web and Interactive Production course.

A javascript-based data visualisation for exploring your Spotify tastes. Uses saved playlists, songs, and the last 50 songs you listened to.

## Usage

To run this on your own computer, use the `static-data` branch and *not* the `master` branch, make a new venv from `requirements.txt` and run `python run.py` in the home directory.
The `master` branch requires the ability to do spotify calls, with the appropriate spotify API creds. For the assignment I have included the `secret_config.py` with those,
but you would also need to be manually added through the spotify developer dashboard, so it's not the most appropriate for this usecase.
If you would like access to that, I need the email address you use for a spotify account, so feel free to get in contact if you need that for grading,
however I've included sample data from my own account

## Code Resources
- [Flask Reference](https://flask.palletsprojects.com/en/2.0.x/)
- [Python 3 Reference](https://docs.python.org/3/)
- [Spotify API Reference](https://developer.spotify.com/documentation/web-api/reference)
- [Spotipy Python Spotify Wrapper](https://github.com/plamere/spotipy)
- [OAuth Tutorial](https://realpython.com/flask-google-login/)

## Design Resources
- [Spotify Design and Branding Guidelines](https://developer.spotify.com/documentation/general/design-and-branding/)
