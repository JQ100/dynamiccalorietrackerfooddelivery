from flask import Blueprint, render_template, request, redirect
from ...models.models import Customer
from ...extensions import db

customer_bp = Blueprint("customer", __name__, template_folder="templates")

@customer_bp.route("/customer", methods=['POST', 'GET'])
def customer():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_customer = Customer(name=name)

        try:
            db.session.add(new_customer)
            db.session.commit()
            return redirect('/customer')
        except:
            return 'There was an issue adding your task'

    else:
        customers = Customer.query.order_by(Customer.created_at).all()
        return render_template('customer_index.html', customers=customers)
