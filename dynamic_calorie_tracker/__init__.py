from flask import Flask, render_template
from .extensions import db

from .blueprints.main.main import main_bp
from .blueprints.personal_info.personal_info import personal_info_bp
from .blueprints.transaction.transaction import transaction_bp
from .blueprints.recipes.recipes import recipes_bp
from .blueprints.restaurant_menu.restaurant_menu import restaurant_menu_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(personal_info_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(restaurant_menu_bp)

    return app
