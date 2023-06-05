from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Item, Genre
from app import app
from lib.db import db
from datetime import datetime
from .sessions import login_check

item = Blueprint('admin_item', __name__, url_prefix='/admin/items')

@item.route('/')
@login_check
def index():
    genre_id = request.args.get('genre_id') or ""  
    if str.isdigit(genre_id):
        items = Item.query.filter_by(genre_id=genre_id).all()
    else:
        items = Item.query.order_by(Item.id).all()
    return render_template('admin/items/index.html', items=items)

@item.route('/new')
@login_check
def new():
    genres = Genre.query.order_by(Genre.id).all()
    return render_template('admin/items/new.html', genres=genres)

@item.route('/create', methods=['POST'])
@login_check
def create():
    file = request.files['image']
    filename = file.filename
    item = Item(
        genre_id = request.form.get('genre_id'),
        name = request.form.get('name'),
        price = request.form.get('price'),
        introduction= request.form.get('introduction'),
        is_active = True if request.form.get('is_active') == '1' else False,
        image_path = app.config['VIEW_IMAGE_PATH'] + filename
    )
    db.session.add(item)
    db.session.commit()
    file.save(app.config['SAVE_IMAGE_PATH'] + filename)
    return redirect(url_for('admin_item.index'))

@item.route('/<int:id>')
def show(id):
    item = Item.query.get(id)
    return render_template('admin/items/show.html', item=item)

@item.route('/<int:id>/edit')
def edit(id):
    item = Item.query.get(id)
    genres = Genre.query.order_by(Genre.id).all()
    return render_template('admin/items/edit.html', item=item, genres=genres)

@item.route('/<int:id>/update', methods=['POST'])
def update(id):
    item = Item.query.get(id)
    file = request.files['image']
    filename = file.filename
    item.name = request.form.get('name')
    item.introduction = request.form.get('introduction')
    item.genre_id = request.form.get('genre_id')
    item.price = request.form.get('price')
    item.is_active = True if request.form.get('is_active') == '1' else False
    item.image_path = app.config['VIEW_IMAGE_PATH'] + filename
    item.updated_at = datetime.now()
    db.session.merge(item)
    db.session.commit()
    file.save(app.config['SAVE_IMAGE_PATH'] + filename)
    return redirect(url_for('admin_item.show', id=item.id))