from flask import Blueprint, render_template, request, redirect
from ...models.restaurant_menu import RestaurantMenu
from ...extensions import db

restaurant_menu_bp = Blueprint(
    "restaurant_menu", 
    __name__, 
    template_folder="templates", 
    static_folder='static',
)


@restaurant_menu_bp.route("/restaurant_menu", methods=["GET", "POST"])
def restaurant_menu():
    if request.method == 'POST':
        name = request.form['name']
        new_restaurant_menu = RestaurantMenu(name=name)

        try:
            db.session.add(new_restaurant_menu)
            db.session.commit()
            return redirect('/restaurant_menu')
        except:
            return 'There was an issue adding your menu'

    else:
        restaurant_menus = RestaurantMenu.query.order_by(
            RestaurantMenu.date_created).all()
        return render_template('menu_index.html', restaurant_menus=restaurant_menus)