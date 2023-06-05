from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Order, Customer
from lib.db import db
from .sessions import login_check
from datetime import datetime

order = Blueprint('admin_order', __name__, url_prefix='/admin/orders')

@order.route('/')
@login_check
def index():
    customer_id = request.args.get('customer_id') or ""  
    customer = ""
    if str.isdigit(customer_id):
        orders = Order.query.filter_by(customer_id=customer_id).all()
        customer = Customer.query.get(customer_id)
    elif request.args.get('created_at'):
        now = datetime.now()
        today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        orders = Order.query.filter_by(created_at=today).all()
    else:
        orders = Order.query.order_by(Order.id).all()
    return render_template('admin/orders/index.html', orders=orders, customer=customer)

@order.route('/<int:id>', methods=['GET'])
@login_check
def show(id):
    order = Order.query.get(id)
    order_items = order.order_items
    return render_template('admin/orders/show.html', order=order, order_items=order_items)

@order.route('/<int:id>', methods=['POST'])
@login_check
def update(id):
    order = Order.query.get(id)
    order.status = int(request.form.get('status'))
    order.updated_at = datetime.now()
    db.session.merge(order)
    db.session.commit()
    # status:{0:'入金待ち', 1:'入金確認', 2:'製作中', 3:'発送準備中', 4:'発送済み'}
    if order.status == 1:
    # making_status:{0:'製作不可', 1:'製作待ち', 2:'製作中', 3:'製作完了'}
        for order_item in order.order_items:
            order_item.making_status = 1
            order_item.updated_at = datetime.now()
            db.session.merge(order_item)
            db.session.commit()
    return redirect(url_for('admin_order.show', id=order.id))    