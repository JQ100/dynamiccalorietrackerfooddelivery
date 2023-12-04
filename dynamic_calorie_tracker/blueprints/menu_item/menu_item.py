from flask import Blueprint, render_template, request, redirect
from ...models.menu_item import MenuItem
from ...extensions import db

menu_item_bp = Blueprint(
    "menu_item", 
    __name__, 
    template_folder="templates", 
    static_folder='static',
)


@menu_item_bp.route("/menu_item", methods=["GET", "POST"])
def menu_item():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_menu_item = MenuItem(name=name)

        try:
            db.session.add(new_menu_item)
            db.session.commit()
            return redirect('/menu_item')
        except:
            return 'There was an issue adding your menu'

    else:
        menu_items = MenuItem.query.order_by(MenuItem.created_at).all()
        return render_template('menu_index.html', menu_items=menu_items)