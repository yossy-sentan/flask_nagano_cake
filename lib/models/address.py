from lib.db import db
from datetime import datetime

class Address(db.Model):

    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    post_code = db.Column(db.String(64), nullable=False, unique=False)
    address = db.Column(db.String(100), nullable=False, unique=False)
    name = db.Column(db.String(64), nullable=False, unique=False)
    created_at = db.Column(db.Date, nullable=False, unique=False)
    updated_at = db.Column(db.Date, nullable=False, unique=False)

    customer = db.relationship('Customer', uselist=False)

    def __init__(self, customer_id, post_code, address, name):
        self.customer_id = customer_id
        self.post_code = post_code
        self.address = address
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def show_address(self):
        return f'〒{self.post_code} {self.address} {self.name}'