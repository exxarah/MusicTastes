from flask import render_template
from flask_login import current_user
from . import general_bp


@general_bp.route('/')
def index():
    print("Index loading")
    if current_user.is_authenticated:
        return render_template('vis.html')
    else:
        return render_template('index.html')
