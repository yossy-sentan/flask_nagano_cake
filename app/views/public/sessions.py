from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Customer
from flask_login import login_user, logout_user, current_user
from lib.db import db

public_session = Blueprint('public_session', __name__)

@public_session.route('/log_in', methods=['GET'])
def new():
    if current_user.is_authenticated:
        return redirect(url_for('customer.show'))
    return render_template('public/sessions/new.html')

@public_session.route('/log_in', methods=['POST'])
def create():
    if current_user.is_authenticated:
        return redirect(url_for('customer.show'))
    customer = Customer.query.filter_by(email = request.form.get('email')).first()
    if customer is not None:
        if not customer.is_active:
            return redirect(url_for('public_session.new'))
        if customer.password == request.form.get('password'):
            login_user(customer)
            flash('ログインに成功しました', 'success')
            return redirect(url_for('customer.show'))
        
    flash('メールアドレスまたはパスワードが異なります。', 'error')
    return redirect(url_for('public_session.new'))

@public_session.route('/logout')
def delete():
    logout_user()
    flash('ログアウトしました', 'success')
    return redirect(url_for('public_session.new'))