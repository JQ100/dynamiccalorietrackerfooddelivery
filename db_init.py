from dynamic_calorie_tracker.models.models import MenuItem, Customer, Restaurant, MealOrder, OrderDetails

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

# add customers
customers = [
    Customer(name="John Doe", daily_calories_goal=2500,
              per_meal_calories_limit=1000),
    Customer(name="Nancy Miller", daily_calories_goal=2000,
             per_meal_calories_limit=1000),
]
db_session.add_all(customers)
db_session.commit()

# add restaurants
restaurants = [
    Restaurant(name="Smack Burgers", category="New American"),
]
db_session.add_all(restaurants)
db_session.commit()

# add menu items
menuItems = [
    MenuItem(name="Cheeseburger", price=4, calories=300, restaurant_id=1),
    MenuItem(name="Hamburger", price=3, calories=250, restaurant_id=1),
    MenuItem(name="Double Krabby Patty", price=5.5, calories=500, restaurant_id=1),
]
db_session.add_all(menuItems)
db_session.commit()

# add orders
orders = [
    MealOrder(name="breakfast", customer_id = 1),
]
db_session.add_all(orders)
db_session.commit()

# add order_details
order_details = [
    OrderDetails(order_id=1, menu_item_id=1),
    OrderDetails(order_id=1, menu_item_id=3),
]
db_session.add_all(order_details)
db_session.commit()
