from flask import Blueprint, render_template, redirect

transaction_bp = Blueprint("transaction", __name__, template_folder="templates")

@transaction_bp.route("/transaction")
def transaction():
    return "This is the Transaction page"