from lib.db import db
from datetime import datetime

class OrderItem(db.Model):

    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    amount = db.Column(db.Integer, nullable=False, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False)
    making_status = db.Column(db.Integer, nullable=False, unique=False)
    created_at = db.Column(db.Date, nullable=False, unique=False)
    updated_at = db.Column(db.Date, nullable=False, unique=False)

    order = db.relationship('Order', uselist=False)
    item = db.relationship('Item', uselist=False)

    making_status_enum = {0:'製作不可', 1:'製作待ち', 2:'製作中', 3:'製作完了'}

    def __init__(self, order_id, item_id, amount, price):
        self.order_id = order_id
        self.item_id = item_id
        self.amount = amount
        self.price = price
        self.making_status = 0
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def making_status_ja(self):
        return OrderItem.making_status_enum[self.making_status]