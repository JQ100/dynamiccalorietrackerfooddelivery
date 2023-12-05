from flask import Blueprint, render_template, request, redirect
from ...models.models import Customer, MealOrder, OrderDetails
from ...extensions import db, db_session
from sqlalchemy import func

food_delivery_bp = Blueprint("food_delivery", __name__, template_folder="templates")


@food_delivery_bp.route("/food_delivery", methods=['POST', 'GET'])
def food_delivery():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_food_delivery = Customer(name=name)

        try:
            db.session.add(new_food_delivery)
            db.session.commit()
            return redirect('/food_delivery')
        except:
            return 'There was an issue adding your task'

    else:
        customers = Customer.query.all()
        return render_template('food_delivery_index.html', customers=customers)
