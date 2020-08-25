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

@main.route("/checkout")
def Checkout():
    return render_template('checkout.html', title='Checkout')

@main.route("/blog")
def blog():
    return render_template('blog.html', title='blog')
