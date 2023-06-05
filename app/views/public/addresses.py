from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Address
from lib.db import db
from datetime import datetime
from flask_login import login_required, current_user

address = Blueprint('address', __name__, url_prefix='/addresses')

@address.route('/', methods=['GET'])
@login_required
def index():
    addresses = current_user.addresses
    return render_template('public/addresses/index.html', addresses=addresses)

@address.route('/', methods=['POST'])
@login_required
def create():
    address = Address(
        customer_id = current_user.id,
        post_code = request.form.get('post_code'),
        address = request.form.get('address'),
        name = request.form.get('name')
    )
    db.session.add(address)
    db.session.commit()
    return redirect(url_for('address.index'))

@address.route('/<int:id>/edit')
@login_required
def edit(id):
    address = Address.query.get(id)
    return render_template('public/addresses/edit.html', address=address)

@address.route('/<int:id>', methods=['POST'])
@login_required
def update(id):
    address = Address.query.get(id)
    address.post_code = request.form.get('post_code')
    address.address = request.form.get('address')
    address.name = request.form.get('name')
    address.updated_at = datetime.now()
    db.session.add(address)
    db.session.commit()
    return redirect(url_for('address.index'))

@address.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    address = Address.query.get(id)
    db.session.delete(address)
    db.session.commit()
    return redirect(url_for('address.index'))