from flask import jsonify, request
from app.core.services.ItemService import ItemService

class ItemController:
    def __init__(self):
        self.service = ItemService()

    def get_items(self):
        items = self.service.get_all_items()
        return jsonify([item.to_dict() for item in items])

    def create_item(self):
        data = request.get_json()
        new_item = self.service.create_item(data)
        return jsonify(new_item.to_dict()), 201
    
    def get_item(self, item_id):
        item = self.service.get_item_by_id(item_id)
        if item:
            return jsonify(item.to_dict())
        return jsonify({"message": "Item not found"}), 404
    
    def update_item(self, item_id):
        data = request.get_json()
        updated_item = self.service.update_item(item_id, data)
        if updated_item:
            return jsonify(updated_item.to_dict())
        return jsonify({"message": "Item not found"}), 404
    
    def delete_item(self, item_id):
        if self.service.delete_item(item_id):
            return jsonify({"message": "Item deleted successfully"}), 204
        return jsonify({"message": "Item not found"}), 404
    
    



   