from ..extensions import db

from datetime import datetime


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(12))
    email = db.Column(db.String(64))
    address = db.Column(db.String(200))
    category = db.Column(db.String(30))

    def __repr__(self):
        return '<Restaurant %r>' % self.id
