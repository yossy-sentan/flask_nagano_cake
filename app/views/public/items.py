from flask import render_template, request, url_for, session, redirect, Blueprint
from lib.models import Item, Genre
from lib.db import db
from flask_login import login_required

item = Blueprint('item', __name__, url_prefix='/items')

@item.route('/')
def index():
    genres = Genre.query.order_by(Genre.id).all()
    genre_id = request.args.get('genre_id') or ""  
    if str.isdigit(genre_id):
        items = Item.query.filter_by(genre_id=genre_id).all()
    else:
        items = Item.query.order_by(Item.id).all()
    items_count = len(items)
    return render_template('public/items/index.html', items=items, genres=genres, items_count=items_count)

@item.route('/<int:id>')
def show(id):
    item = Item.query.get(id)
    genres = Genre.query.order_by(Genre.id).all()
    return render_template('public/items/show.html', genres=genres, item=item)