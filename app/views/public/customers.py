from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Customer
from lib.db import db
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from app import login_manager

@login_manager.user_loader
def load_customer(customer_id):
    return Customer.query.get(customer_id)

customer = Blueprint('customer', __name__)

@customer.route('/sign_up', methods=['GET'])
def new():
    if current_user.is_authenticated:
        return redirect(url_for('customer.show'))
    return render_template('public/customers/new.html')

@customer.route('/sign_up', methods=['POST'])
def create():
    if current_user.is_authenticated:
        return redirect(url_for('customer.show'))
    if request.form.get('password') == request.form.get('confirm_password'):
        customer = Customer(
            last_name = request.form.get('last_name'),
            first_name = request.form.get('first_name'),
            last_name_kana = request.form.get('last_name_kana'),
            first_name_kana = request.form.get('last_name_kana'),
            post_code = request.form.get('post_code'),
            address = request.form.get('address'),
            tel_number = request.form.get('tel_number'),
            email = request.form.get('email'),
            password = request.form.get('password')
        )
        db.session.add(customer)
        db.session.commit()
        login_user(customer)
    else:
        flash('パスワードが違います', 'error')
        return redirect(url_for('cusotmer.new'))
    return redirect(url_for('customer.show'))

@customer.route('/my_page')
@login_required
def show():
    return render_template('public/customers/show.html')

@customer.route('/customers/edit')
@login_required
def edit():
    return render_template('public/customers/edit.html')

@customer.route('/customer', methods=['POST'])
@login_required
def update():
    customer = current_user
    customer.last_name = request.form.get('last_name')
    customer.first_name = request.form.get('first_name')
    customer.last_name_kana = request.form.get('last_name_kana')
    customer.first_name_kana = request.form.get('last_name_kana')
    customer.post_code = request.form.get('post_code')
    customer.address = request.form.get('address')
    customer.tel_number = request.form.get('tel_number')
    customer.email = request.form.get('email')
    customer.updated_at = datetime.now()
    db.session.merge(customer)
    db.session.commit()
    return redirect(url_for('customer.show'))

@customer.route('/unsubscribe')
@login_required
def unsubscribe():
    return render_template('public/customers/unsubscribe.html')

@customer.route('/withdraw', methods=['POST'])
@login_required
def withdraw():
    customer = current_user
    customer.is_active = False
    db.session.merge(customer)
    db.session.commit()
    logout_user()
    return redirect(url_for('homes.top'))