from lib.db import db
from datetime import datetime

class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    total_price = db.Column(db.Integer, nullable=False, unique=False)
    shipping_cost = db.Column(db.Integer, nullable=False, unique=False)
    post_code = db.Column(db.String(64), nullable=False, unique=False)
    address = db.Column(db.String(100), nullable=False, unique=False)
    name = db.Column(db.String(64), nullable=False, unique=False)
    payment_method = db.Column(db.Integer, nullable=False, unique=False)
    status = db.Column(db.Integer, nullable=False, unique=False)
    created_at = db.Column(db.Date, nullable=False, unique=False)
    updated_at = db.Column(db.Date, nullable=False, unique=False)

    customer = db.relationship('Customer', uselist=False)
    order_items = db.relationship('OrderItem', uselist=True)

    payment_method_enum = {0:'クレジットカード', 1:'銀行振込', 2:'代引き', 3:'PayPay'}
    status_enum = {0:'入金待ち', 1:'入金確認', 2:'製作中', 3:'発送準備中', 4:'発送済み'}

    def __init__(self, customer_id, total_price, shipping_cost, post_code, address, name, payment_method):
        self.customer_id = customer_id
        self.total_price = total_price
        self.shipping_cost = shipping_cost
        self.post_code = post_code
        self.address = address
        self.name = name
        self.payment_method = payment_method
        self.status = 0
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def payment_method_ja(self):
        return Order.payment_method_enum[self.payment_method]
    
    def status_ja(self):
        return Order.status_enum[self.status]
    
    def show_address(self):
        return f'〒{self.post_code} {self.address} {self.name}'
    
    def order_items_amount(self):
        amount = 0
        for order_item in self.order_items:
            amount += order_item.amount
        return amount