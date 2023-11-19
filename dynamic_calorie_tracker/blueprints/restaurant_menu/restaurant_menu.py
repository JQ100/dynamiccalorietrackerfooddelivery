from flask import Blueprint, render_template, redirect
# from blueprints.restaurant_menu.restaurant import Restaurant

restaurant_menu_bp = Blueprint("restaurant_menu", __name__, template_folder="templates")

@restaurant_menu_bp.route("/restaurant_menu")
def restaurant_menu():
    return "This is the Restaurant Menu page. Please choose from the available options."
