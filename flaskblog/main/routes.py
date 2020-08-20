from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')



@main.route("/about")
def about():
    return render_template('landing.html', title='About')


@main.route("/stats")
def stats():
    return render_template('charts.html', title='stats')