from flask import Blueprint, render_template, request, redirect
from ...models.menu_item import MenuItem
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
        # todo
        name = request.form['name']
        new_restaurant_menu = MenuItem(name=name)

        try:
            db.session.add(new_restaurant_menu)
            db.session.commit()
            return redirect('/restaurant_menu')
        except:
            return 'There was an issue adding your menu'

    else:
        menu_items = MenuItem.query.order_by(MenuItem.created_at).all()
        return render_template('menu_index.html', menu_items=menu_items)
