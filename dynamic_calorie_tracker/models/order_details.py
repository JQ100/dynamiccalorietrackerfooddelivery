from ..extensions import db
from datetime import datetime

# check out https://stackoverflow.com/questions/51335298/concepts-of-backref-and-back-populate-in-sqlalchemy
# for relationship() and back_ref
class OrderDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('meal_order.id'))
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    meal_order = db.relationship("MealOrder", backref="OrderDetails")
    menu_item = db.relationship("MenuItem", backref="OrderDetails")
    
    def __repr__(self):
        return '<OrderDetails %r>' % self.id
