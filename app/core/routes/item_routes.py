from flask import Blueprint
from app.core.controllers.ItemController import ItemController

mod = Blueprint('item', __name__, ) 
item_controller = ItemController()

@mod.route('/', methods=['GET'])
def get_items():
    return item_controller.get_items()

@mod.route('/', methods=['POST'])
def create_item():
    return item_controller.create_item()

@mod.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return item_controller.get_item(item_id)

@mod.route('/category/<int:category_id>', methods=['GET'])
def get_items_by_category(category_id):
    return item_controller.get_items_by_category(category_id)

@mod.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return item_controller.update_item(item_id)

@mod.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return item_controller.delete_item(item_id)


def items_routes(app):
    app.register_blueprint(mod, url_prefix='/api/v1/items')
