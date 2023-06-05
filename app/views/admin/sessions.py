from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from functools import wraps
from app import app

def login_check(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('ログインしてください', 'error')
            return redirect(url_for('admin_session.new'))
        return view(*args, **kwargs)
    return inner

admin_session = Blueprint('admin_session', __name__, url_prefix='/admin')

@admin_session.route('/login', methods=['GET'])
def new():
    return render_template('admin/sessions/new.html')

@admin_session.route('/login', methods=['POST'])
def create():
    if request.form.get('admin_id') != app.config['ADMIN_ID']:
        flash('管理者IDが異なります', 'error')
    elif request.form.get('password') != app.config['ADMIN_PASSWORD']:
        flash('パスワードが異なります', 'error')
    else:
        session['admin_logged_in'] = True
        return redirect(url_for('admin_home.top'))
    return render_template('admin/sessions/new.html')

@admin_session.route('/logout')
def delete():
    session.pop('admin_logged_in', None)
    flash('ログアウトしました', 'success')
    return redirect(url_for('admin_session.new'))