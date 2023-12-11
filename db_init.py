from dynamic_calorie_tracker.models.models import MenuItem, Customer, Restaurant, MealOrder, OrderItem

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

# Delete old data in the tables
db_session.query(Customer).delete()
db_session.query(Restaurant).delete()
db_session.query(MenuItem).delete()
db_session.query(MealOrder).delete()
db_session.query(OrderItem).delete()
db_session.commit()

# add customers
customers = [
    Customer(name="John Doe", daily_calories_goal=2800,
              per_meal_calories_limit=1000),
    Customer(name="Nancy Miller", daily_calories_goal=2300,
             per_meal_calories_limit=1000),
]
db_session.add_all(customers)
db_session.commit()

# add restaurants
restaurants = [
    Restaurant(name="Smack Burgers", phone="123-456-7890",
               email="dummy@mail.com", address="dummy address"),
]
db_session.add_all(restaurants)
db_session.commit()

# add menu items
# todo: add items with low calories to fill in an order.
menuItems = [
    MenuItem(name="Cheeseburger", price=4, calories=300, restaurant_id=1),
    MenuItem(name="Hamburger", price=3, calories=250, restaurant_id=1),
    MenuItem(name="Double Krabby Patty", price=5.5, calories=500, restaurant_id=1),
    MenuItem(name="Double Krabby Patty with Cheese", price=7.5, calories=650, restaurant_id=1),
    MenuItem(name="French Fries Plate", price=5, calories=480, restaurant_id=1),
    MenuItem(name="Wild Pollock Fish & Chips", price=15, calories=710, restaurant_id=1),
    MenuItem(name="Coleslaw", price=2.5, calories=290, restaurant_id=1),
    MenuItem(name="10 pc Chicken Nuggets", price=8, calories=520, restaurant_id=1),
    MenuItem(name="2 pc Chicken Nuggets", price=2, calories=104, restaurant_id=1),
    MenuItem(name="5 pc Chicken Tenders", price=7, calories=740, restaurant_id=1),
    MenuItem(name="5 pc Chicken Wings", price=5, calories=700, restaurant_id=1),
    MenuItem(name="Filet O Fish", price=2.5, calories=390, restaurant_id=1),
    MenuItem(name="Salad", price=3.5, calories=100, restaurant_id=1),
    MenuItem(name="Soup", price=4.5, calories=130, restaurant_id=1),
    MenuItem(name="Burrito", price=6, calories=400, restaurant_id=1),
    MenuItem(name="Baby Carrots", price=1, calories=50, restaurant_id=1)
]
db_session.add_all(menuItems)
db_session.commit()

# Do not need to add orders

# Do not need to add OrderItem
