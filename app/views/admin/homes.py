from flask import render_template, request, session, Blueprint
from lib.models import Order
from datetime import datetime
from .sessions import login_check

home = Blueprint('admin_home', __name__, url_prefix='/admin')

@home.route('/')
@login_check
def top():
    now = datetime.now()
    today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    count = Order.query.filter_by(created_at=today).count()
    return render_template('admin/homes/top.html', count=count)