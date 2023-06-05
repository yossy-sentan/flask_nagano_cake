from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import Item
from lib.db import db
from flask_login import login_required

cart = Blueprint('cart', __name__, url_prefix='/carts')

@cart.route('/', methods=['POST'])
@login_required
def create():
    item_id = request.form.get('item_id')
    amount = request.form.get('amount')

    cart = session.get('cart')
    if type(cart) is dict:
        origin_amount = cart.get(item_id) or 0
        cart[item_id] = origin_amount + int(amount)
    else:
        cart = {item_id: int(amount)}
    session['cart'] = cart
    return redirect(url_for('cart.index'))

@cart.route('/', methods=['GET'])
@login_required
def index():
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

    return render_template('public/carts/index.html', cart_items=cart_items, total_price=total_price)

@cart.route('/<string:item_id>', methods=['POST'])
@login_required
def update(item_id):
    cart = session.get('cart')
    cart[item_id] = request.form.get('amount')
    session['cart'] = cart
    return redirect(url_for('cart.index'))

@cart.route('/<string:item_id>/delete')
@login_required
def delete(item_id):
    if item_id == 'all':
        session.pop('cart', None)
    else:
        cart = session.get('cart')
        cart.pop(item_id, None)
        session['cart'] = cart
    flash('商品がカートから削除されました', 'success')
    return redirect(url_for('cart.index'))
    
