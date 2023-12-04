from ..extensions import db

from datetime import datetime


class MealOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<MealOrder %r>' % self.id
