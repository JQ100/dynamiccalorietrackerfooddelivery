from flask import Blueprint, render_template, request, redirect
from ...models.order_details import OrderDetails
from ...extensions import db

order_details_bp = Blueprint("order_details", __name__, template_folder="templates")


@order_details_bp.route("/order_details", methods=['POST', 'GET'])
def order_details():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_order_details = OrderDetails(name=name)

        try:
            db.session.add(new_order_details)
            db.session.commit()
            return redirect('/order_details')
        except:
            return 'There was an issue adding your task'

    else:
        order_details = OrderDetails.query.order_by(OrderDetails.created_at).all()
        # todo: use render_template
        # return render_template('index.html', tasks=tasks)
        return "This is the order details page"
