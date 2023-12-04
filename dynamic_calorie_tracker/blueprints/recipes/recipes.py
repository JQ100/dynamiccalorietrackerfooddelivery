from flask import Blueprint, render_template, redirect

recipes_bp = Blueprint("recipes", __name__, template_folder="templates")

@recipes_bp.route("/recipes")
def recipes():
    return render_template('recipe.html')

# python -m flask -app