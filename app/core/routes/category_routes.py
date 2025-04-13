from flask import Blueprint
from app.core.controllers.CategoryController import CategoryController

mod = Blueprint('category', __name__, ) 
category_controller = CategoryController()

@mod.route('/', methods=['GET'])
def get_items():
    return category_controller.get_categories()

@mod.route('/', methods=['POST'])
def create_item():
    return category_controller.create_category()


def categories_routes(app):
    app.register_blueprint(mod, url_prefix='/api/v1/categories')
