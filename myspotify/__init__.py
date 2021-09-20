""" MAIN FILE """
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

# Database Setup
db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'myspotify.sqlite')
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
        # Database Setup

        from myspotify.auth.models import User

        db.init_app(app)
        db.create_all()

        from myspotify.general import general_bp
        from myspotify.auth import auth_bp

        # Blueprints Setup
        app.register_blueprint(general_bp, url_prefix='/')
        app.register_blueprint(auth_bp, url_prefix='/')

        login_manager = LoginManager()
        login_manager.login_view = 'auth_bp.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        return app


app = create_app()
