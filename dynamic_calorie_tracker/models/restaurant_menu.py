from ..extensions import db

from datetime import datetime


class RestaurantMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<RestaurantMenu %r>' % self.id
