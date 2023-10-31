from flask import Flask, render_template
from blueprints.personalinfo.personalinfo import personalinfo_bp
from blueprints.transaction.transaction import transaction_bp
from blueprints.recipes.recipes import recipes_bp
from  blueprints.restaurantmenu.restaurantmenu import restaurantmenu_bp

DynamicCalorieTracker = Flask(__name__)
DynamicCalorieTracker.register_blueprint(personalinfo_bp)
DynamicCalorieTracker.register_blueprint(transaction_bp)
DynamicCalorieTracker.register_blueprint(recipes_bp)
DynamicCalorieTracker.register_blueprint(restaurantmenu_bp)

@DynamicCalorieTracker.route("/")
def index():
    return render_template('index.html');
