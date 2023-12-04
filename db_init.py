from sqlalchemy import create_engine
from dynamic_calorie_tracker import db
from dynamic_calorie_tracker.extensions import db
from dynamic_calorie_tracker import create_app
from dynamic_calorie_tracker.models import *

from sqlalchemy.orm import Session

# create all the tables in models directory
db.create_all(app=create_app())

# initialize a db session
engine = create_engine('sqlite:///dynamic_calorie_tracker/db.sqlite3', echo=True)
db_session = Session(engine)

# add menu items
from dynamic_calorie_tracker.models.menu_item import MenuItem
menuItems = [
    MenuItem(name="Cheeseburger", price=4, calories=300, restaurant_id=1),
    MenuItem(name="Hamburger", price=3, calories=250, restaurant_id=1),
    MenuItem(name="Double Krabby Patty", price=5.5, calories=500, restaurant_id=1),
]
db_session.add_all(menuItems)
db_session.commit()
