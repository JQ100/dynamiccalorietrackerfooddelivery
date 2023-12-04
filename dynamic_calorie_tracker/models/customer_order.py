from ..extensions import db

from datetime import datetime

# May add the username and password but they are not used in this project.


class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('meal_order.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    customer = db.relationship("Customer", backref="CustomerOrder")
    meal_order = db.relationship("MealOrder", backref="CustomerOrder")

    def __repr__(self):
        return '<CustomerOrder %r>' % self.id
