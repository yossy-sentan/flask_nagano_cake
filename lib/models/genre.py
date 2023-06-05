from lib.db import db
from datetime import datetime

class Genre(db.Model):

    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    created_at = db.Column(db.Date, nullable=False, unique=False)
    updated_at = db.Column(db.Date, nullable=False, unique=False)

    items = db.relationship('Item', uselist=True)

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at