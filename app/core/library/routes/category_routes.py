from flask import Blueprint
from app.core.library.controllers.CategoryController import CategoryController

mod = Blueprint('category', __name__, ) 
category_controller = CategoryController()

@mod.route('/', methods=['GET'])
def get_items():
    return category_controller.get_categories()

@mod.route('/', methods=['POST'])
def create_item():
    return category_controller.create_category()

@mod.route('/<int:category_id>', methods=['GET'])
def get_item(category_id):
    return category_controller.get_category_by_id(category_id)

@mod.route('/<int:category_id>', methods=['PUT'])
def update_item(category_id):
    return category_controller.update_category(category_id)

@mod.route('/<int:category_id>', methods=['DELETE'])
def delete_item(category_id):
    return category_controller.delete_category(category_id)



def categories_routes(app):
    app.register_blueprint(mod, url_prefix='/api/v1/categories')
