from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Genre
from lib.db import db
from datetime import datetime
from .sessions import login_check

genre = Blueprint('admin_genre', __name__, url_prefix="/admin/genres")

@genre.route('/')
@login_check
def index():
    genres = Genre.query.order_by(Genre.id).all()
    return render_template('admin/genres/index.html', genres=genres)

@genre.route('/create', methods=['POST'])
@login_check
def create():
    genre = Genre(
        name = request.form.get('name')
    )
    try:
        db.session.add(genre)
        db.session.commit()
    except:
        flash('入力した値を確認してください', 'error')
    return redirect(url_for('admin_genre.index'))

@genre.route('/<int:id>/edit')
@login_check
def edit(id):
    genre = Genre.query.get(id)
    return render_template('admin/genres/edit.html', genre=genre)

@genre.route('/<int:id>/update', methods=['POST'])
@login_check
def update(id):
    genre = Genre.query.get(id)
    genre.name = request.form.get('name')
    genre.updated_at = datetime.now()
    try:
        db.session.merge(genre)
        db.session.commit()
    except:
        flash('入力した値を確認してください', 'error')
        return redirect(url_for('admin_genre.edit', id=id))
    return redirect(url_for('admin_genre.index'))