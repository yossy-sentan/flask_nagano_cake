from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Item, Genre
from lib.db import db
# from .sessions import login_check

home = Blueprint('home', __name__)

@home.route('/')
def top():
    items = Item.query.order_by(Item.id.desc()).limit(4)
    genres = Genre.query.order_by(Genre.id).all()
    return render_template('public/homes/top.html', items=items, genres=genres)

@home.route('/about')
def about():
    return render_template('public/homes/about.html')