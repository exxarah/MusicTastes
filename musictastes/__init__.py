""" MAIN FILE """
import spotipy
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from spotipy import oauth2
import os

# Setup
global app, db


def database_setup():
    # Database Setup
    global db
    db = SQLAlchemy()

    db.init_app(app)
    db.create_all()


def blueprints_setup():
    from musictastes.general import general_bp

    # Blueprints Setup
    app.register_blueprint(general_bp, url_prefix='/')


def create_app(test_config=None):
    global app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'musictastes.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_object('config')
    else:
        # Load the test_config if passed if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    with app.app_context():
        database_setup()
        blueprints_setup()

        return app


app = create_app()
