from flask import Blueprint, render_template, redirect
from blueprints.restaurantmenu.restaurant import Restaurant

restaurantmenu_bp = Blueprint("restaurantmenu", __name__, template_folder="templates")

@restaurantmenu_bp.route("/restaurantmenu")
def restaurantmenu():
    return "This is the Restaurant Menu page. Please choose from the available options."