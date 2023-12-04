from flask import Blueprint, render_template, request, redirect
from ...models.restaurant import Restaurant
from ...extensions import db

restaurant_bp = Blueprint(
    "restaurant",
    __name__,
    template_folder="templates",
    static_folder='static',
)


@restaurant_bp.route("/restaurant", methods=["GET", "POST"])
def restaurant():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_restaurant = Restaurant(name=name)

        try:
            db.session.add(new_restaurant)
            db.session.commit()
            return redirect('/restaurant')
        except:
            return 'There was an issue adding your menu'

    else:
        restaurants = Restaurant.query.order_by(Restaurant.created_at).all()
        # return render_template('menu_index.html', restaurants=restaurants)
