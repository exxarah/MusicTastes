from flask import render_template
from . import auth_bp


@auth_bp.route('/')
def index():
    return render_template('login.html')