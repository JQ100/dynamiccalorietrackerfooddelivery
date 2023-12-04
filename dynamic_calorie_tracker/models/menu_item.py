from ..extensions import db

from datetime import datetime


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    restaurant = db.relationship("Restaurant", backref="MenuItem")

    def __repr__(self):
        return '<MenuItem %r>' % self.id
