from flask import render_template, request, url_for, session, redirect, flash, Blueprint
from lib.models import OrderItem
from lib.db import db
from datetime import datetime
from .sessions import login_check

order_item = Blueprint('admin_order_item', __name__, url_prefix='/admin/order_items')

@order_item.route('/<int:id>', methods=['POST'])
@login_check
def update(id):
    order_item = OrderItem.query.get(id)
    order = order_item.order
    if order.status == 0:
        flash('まだ入金が確認されていません', 'error')
    else:
        order_item.making_status = int(request.form.get('making_status'))
        order_item.updated_at = datetime.now()
        db.session.merge(order_item)
        db.session.commit()
        # making_status:{0:'製作不可', 1:'製作待ち', 2:'製作中', 3:'製作完了'}
        # order.status:{0:'入金待ち', 1:'入金確認', 2:'製作中', 3:'発送準備中', 4:'発送済み'}
        if (order_item.making_status == 2) and (order.status != 2):
            order.status = 2
            order_item.updated_at = datetime.now()
            db.session.merge(order)
            db.session.commit()
        elif len(order.order_items) == sum(oi.making_status==3 for oi in order.order_items):
            order.status = 3
            order_item.updated_at = datetime.now()
            db.session.merge(order)
            db.session.commit()
    return redirect(url_for('admin_order.show', id=order.id))