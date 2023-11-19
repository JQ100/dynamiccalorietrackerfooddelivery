from flask import Blueprint, render_template, redirect

recipes_bp = Blueprint("recipes", __name__, template_folder="templates")

@recipes_bp.route("/recipes")
def recipes():
    return "This is the Recipe page"