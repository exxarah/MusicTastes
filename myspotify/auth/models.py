""" Data Models for User Functionality """
import datetime
from flask_login import UserMixin
from myspotify import db


class User(UserMixin, db.Model):
    """
    User Model Data. Store user information
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    recipes = db.relationship('Recipe', backref="user_object", lazy=True)
    likes = db.relationship('Like', backref="user_object", lazy=True)
    ratings = db.relationship('Rating', backref="user_object", lazy=True)
    bio = db.Column(db.String(1024), nullable=True)

    def __init__(self, email, username, password, admin=False):
        self.email = email
        self.username = username
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin
