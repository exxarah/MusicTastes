import os


def get_recently_played(spotify):
    return spotify.current_user_recently_played()


def fake_recently_played(spotify):
    result = ""
    with open(
            os.path.join(os.path.dirname(__file__),'..\\static\\data\\recently_played.txt'),
            'r',
            encoding='utf-8'
    ) as f:
        result = f.read()
    return result


def get_saved_tracks(spotify):
    result = []
    offset = 0
    increment = 20
    while True:
        result.append(spotify.current_user_saved_tracks(offset=offset, limit=increment))
        if not result[-1]["next"]:
            break
        offset += increment
    return result


def fake_saved_tracks(spotify):
    result = ""
    with open(
            os.path.join(os.path.dirname(__file__), '..\\static\\data\\saved_tracks.txt'),
            'r',
            encoding='utf-8'
    ) as f:
        result = f.read()
    return result


def get_current_user(spotify):
    return spotify.current_user()


def fake_current_user(spotify):
    result = ""
    with open(
            os.path.join(os.path.dirname(__file__), '..\\static\\data\\user_profile.txt'),
            'r',
            encoding='utf-8'
    ) as f:
        result = f.read()
    return result
