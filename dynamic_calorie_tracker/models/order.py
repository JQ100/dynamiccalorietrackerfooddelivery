from ..extensions import db

from datetime import datetime


class MealOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    customer = db.relationship("Customer", backref="MealOrder")

    def __repr__(self):
        return '<MealOrder %r>' % self.id
