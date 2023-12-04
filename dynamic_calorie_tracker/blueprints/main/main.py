from flask import Blueprint, render_template
from dynamic_calorie_tracker.blueprints.restaurant_menu.restaurant_menu import restaurantCalories

totalCalories = restaurantCalories

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template('index.html', total_calories=totalCalories);
