from flask import Blueprint, render_template, request, redirect
from ...models.customer_order import CustomerOrder
from ...extensions import db

customer_order_bp = Blueprint(
    "customer_order",
    __name__,
    template_folder="templates",
    static_folder='static',
)


@customer_order_bp.route("/customer_order", methods=["GET", "POST"])
def customer_order():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_customer_order = CustomerOrder(name=name)

        try:
            db.session.add(new_customer_order)
            db.session.commit()
            return redirect('/customer_order')
        except:
            return 'There was an issue adding your menu'

    else:
        customer_orders = CustomerOrder.query.order_by(CustomerOrder.created_at).all()
        # return render_template('menu_index.html', customer_orders=customer_orders)
