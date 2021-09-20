from flask import render_template
from . import auth_bp


@auth_bp.route('/login')
def login():
    print("login")
    return render_template('login.html')
