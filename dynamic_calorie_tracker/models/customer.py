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
