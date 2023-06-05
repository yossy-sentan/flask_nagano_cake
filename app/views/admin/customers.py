from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Customer
from lib.db import db
from datetime import datetime
from .sessions import login_check

customer = Blueprint('admin_customer', __name__, url_prefix='/admin/customers')

@customer.route('/')
@login_check
def index():
    customers = Customer.query.order_by(Customer.id).all()
    return render_template('admin/customers/index.html', customers=customers)

@customer.route('/<int:id>', methods=['GET'])
@login_check
def show(id):
    customer = Customer.query.get(id)
    return render_template('admin/customers/show.html', customer=customer)

@customer.route('/<int:id>/edit')
@login_check
def edit(id):
    customer = Customer.query.get(id)
    return render_template('admin/customers/edit.html', customer=customer)

@customer.route('/<int:id>', methods=['POST'])
@login_check
def update(id):
    customer = Customer.query.get(id)
    customer.last_name = request.form.get('last_name')
    customer.first_name = request.form.get('first_name')
    customer.last_name_kana = request.form.get('last_name_kana')
    customer.first_name_kana = request.form.get('last_name_kana')
    customer.post_code = request.form.get('post_code')
    customer.address = request.form.get('address')
    customer.tel_number = request.form.get('tel_number')
    customer.email = request.form.get('email')
    customer.is_active = True if request.form.get('is_active') == '1' else False
    customer.updated_at = datetime.now()
    db.session.add(customer)
    db.session.commit()
    return redirect(url_for('admin_customer.show', id=customer.id))