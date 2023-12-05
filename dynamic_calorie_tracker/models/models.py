from ..extensions import db

from datetime import datetime

# May add the username and password but they are not used in this project.
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    daily_calories_goal = db.Column(db.Integer)
    per_meal_calories_limit = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Customer %r>' % self.id


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(12))
    email = db.Column(db.String(64))
    address = db.Column(db.String(200))
    category = db.Column(db.String(30))

    def __repr__(self):
        return '<Restaurant %r>' % self.id


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # category can be appetizer, side, soup, salad or main course
    # so that we do not order too many main courses in one meal
    category = db.Column(db.String(20))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    restaurant = db.relationship("Restaurant", backref="MenuItem")

    def __repr__(self):
        return '<MenuItem %r>' % self.id


class MealOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # breakfast, lunch, snack, etc.
    name = db.Column(db.String(20))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    # payment = item prices + tips + taxes + delivery fee
    payment = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    customer = db.relationship("Customer", backref="MealOrder")

    def __repr__(self):
        return '<MealOrder %r>' % self.id


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
