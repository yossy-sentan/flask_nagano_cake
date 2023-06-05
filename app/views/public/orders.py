from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Order, Address, Item, OrderItem
from lib.db import db
from flask_login import login_required, current_user

order = Blueprint('order', __name__, url_prefix='/orders')

@order.route('/new')
@login_required
def new():
    addresses = current_user.addresses
    return render_template('public/orders/new.html', addresses=addresses)

@order.route('/confirm', methods=['GET', 'POST'])
@login_required
def confirm():
    if request.method == 'GET':
        return render_template('public/orders/error.html')
    cart = session.get('cart')
    cart_items = list()
    total_price = 0
    if type(cart) is dict:
        for item_id, amount in cart.items():
            item = Item.query.get(int(item_id))
            amount = int(amount)
            sub_total = item.with_tax_price() * amount
            total_price += sub_total
            cart_items.append({'item': item, 'amount': amount, 'sub_total': sub_total})
    shipping_cost = 800
    order = Order(None, None, None, None, None, None, None)
    order.shipping_cost = shipping_cost
    order.total_price = total_price + shipping_cost
    order.payment_method = int(request.form.get('payment_method'))
    if request.form.get('selected_address') == '0':
        order.post_code = current_user.post_code
        order.address = current_user.address
        order.name = current_user.full_name()
    elif request.form.get('selected_address') == '1':
        address = Address.query.get(request.form.get('address_id'))
        order.post_code = address.post_code
        order.address = address.address
        order.name = address.name
    else:
        order.post_code = request.form.get('post_code')
        order.address = request.form.get('address')
        order.name = request.form.get('name')
    return render_template('public/orders/confirm.html', cart_items=cart_items, order=order, item_total_price=total_price)

@order.route('/', methods=["POST"])
@login_required
def create():
    order = Order(
        customer_id = current_user.id,
        total_price = request.form.get('total_price'),
        shipping_cost = 800,
        post_code = request.form.get('post_code'),
        address = request.form.get('address'),
        name = request.form.get('name'),
        payment_method = request.form.get('payment_method')
    )
    db.session.add(order)
    db.session.commit()

    cart = session.get('cart')
    if type(cart) is dict:
        for item_id, amount in cart.items():
            item = Item.query.get(int(item_id))
            order_item = OrderItem(
                order_id = order.id,
                item_id = item.id,
                amount = int(amount),
                price = item.with_tax_price()
            )
            db.session.add(order_item)
            db.session.commit()
        session.pop('cart', None)
        
    return redirect(url_for('order.thanks'))

@order.route('/thanks')
@login_required
def thanks():
    return render_template('public/orders/thanks.html')

@order.route('/')
@login_required
def index():
    orders = current_user.orders
    return render_template('public/orders/index.html', orders=orders)

@order.route('/<int:id>')
@login_required
def show(id):
    order = Order.query.get(id)
    order_items = order.order_items
    return render_template('public/orders/show.html', order=order, order_items=order_items)