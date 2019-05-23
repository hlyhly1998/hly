from flask import Blueprint, render_template

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/about/')
def about():
    return render_template('about.html')