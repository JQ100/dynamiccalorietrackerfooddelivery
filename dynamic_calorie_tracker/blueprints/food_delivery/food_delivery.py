from flask import Blueprint, render_template, request, redirect
from ...models.models import Customer, MealOrder, OrderDetails
from ...extensions import db, db_session, db_engine
from sqlalchemy import func, select
from datetime import datetime

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
        # orders = MealOrder.query.filter_by(created_at=datetime.now().date()).group_by(MealOrder.customer_id).all()
        # select sum(calories) from menu_item where menu_item.id in 
        # (select id from order_details where order_id in 
        # (select id from meal_order where date(created_at, 'localtime') = date('now', 'localtime') 
        # group by customer_id)); 
        # rs = db_session.query(MealOrder.cls, func.sum(MealOrder.cert_count)) \
        #     .group_by(MealOrder.cls).all()
        # orders = db_session.query(func.sum(MealOrder.id), MealOrder.customer_id) \
        #     .group_by(MealOrder.customer_id).all()
        # print(orders)
        return render_template('food_delivery_index.html', customers=customers)

# @food_delivery_bp.route("/food_delivery")
# def 