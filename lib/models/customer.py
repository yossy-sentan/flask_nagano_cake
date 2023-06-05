from lib.db import db
from flask_login import UserMixin
from datetime import datetime

class Customer(UserMixin, db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), nullable=False, unique=False)
    first_name = db.Column(db.String(64), nullable=False, unique=False)
    last_name_kana = db.Column(db.String(64), nullable=False, unique=False)
    first_name_kana = db.Column(db.String(64), nullable=False, unique=False)
    post_code = db.Column(db.String(64), nullable=False, unique=False)
    address = db.Column(db.String(100), nullable=False, unique=False)
    tel_number = db.Column(db.String(20), nullable=False, unique=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False, unique=False)
    is_active = db.Column(db.Boolean, nullable=False, unique=False)
    created_at = db.Column(db.Date, nullable=False, unique=False)
    updated_at = db.Column(db.Date, nullable=False, unique=False)
    
    addresses = db.relationship('Address', uselist=True)
    orders = db.relationship('Order', uselist=True)

    def __init__(self, last_name, first_name, last_name_kana, first_name_kana, post_code, address, tel_number, email, password):
        self.last_name = last_name
        self.first_name = first_name
        self.last_name_kana = last_name_kana
        self.first_name_kana = first_name_kana
        self.post_code = post_code
        self.address = address
        self.tel_number = tel_number
        self.email = email
        self.password = password
        self.is_active = True
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def full_name(self):
        return self.last_name + self.first_name
    
    def full_name_kana(self):
        return self.last_name_kana + self.first_name_kana
    
    def show_address(self):
        return f'〒{self.post_code} {self.address} {self.full_name()}'