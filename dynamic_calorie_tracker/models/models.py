from ..extensions import db

from datetime import datetime

# May add the username and password but they are not used in this project.
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    daily_calories_goal = db.Column(db.Integer)
    per_meal_calories_limit = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Customer %r>' % self.id


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(12))
    email = db.Column(db.String(64))
    address = db.Column(db.String(200))

    def __repr__(self):
        return '<Restaurant %r>' % self.id


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())

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
    # use date instead of datetime for easy query of daily meals
    created_at = db.Column(db.Date, default=datetime.now().date())

    customer = db.relationship("Customer", backref="MealOrder")

    def __repr__(self):
        return '<MealOrder %r>' % self.id


# check out https://stackoverflow.com/questions/51335298/concepts-of-backref-and-back-populate-in-sqlalchemy
# for relationship() and back_ref
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('meal_order.id'))
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())

    meal_order = db.relationship("MealOrder", backref="OrderItem")
    menu_item = db.relationship("MenuItem", backref="OrderItem")

    def __repr__(self):
        return '<OrderItem %r>' % self.id
