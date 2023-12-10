from flask import Blueprint, render_template, request, redirect
from ...models.models import MealOrder
from ...extensions import db

order_bp = Blueprint("order", __name__, template_folder="templates")


@order_bp.route("/order", methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_order = MealOrder(name=name)

        try:
            db.session.add(new_order)
            db.session.commit()
            return redirect('/order')
        except:
            return 'There was an issue adding your task'

    else:
        orders = MealOrder.query.order_by(MealOrder.created_at).all()
        return render_template('order_index.html', orders=orders)
