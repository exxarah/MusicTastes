from flask import render_template
from . import general_bp


@general_bp.route('/')
def index():
    print("Index loading")
    return render_template('index.html')
