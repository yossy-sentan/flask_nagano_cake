from lib.db import db
from datetime import datetime

class Item(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    name = db.Column(db.String(64), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False, unique=False)
    introduction = db.Column(db.String(100), nullable=False, unique=False)
    image_path = db.Column(db.String(100), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, nullable=False, unique=False)
    created_at = db.Column(db.Date, nullable=False, unique=False)
    updated_at = db.Column(db.Date, nullable=False, unique=False)

    genre = db.relationship('Genre', uselist=False)

    def __init__(self, genre_id, name, price, introduction, is_active, image_path='static/images/no_image.png'):
        self.genre_id = genre_id
        self.name = name
        self.price = price
        self.introduction = introduction
        self.image_path = image_path
        self.is_active = is_active
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def with_tax_price(self):
        return int(self.price * 1.1)