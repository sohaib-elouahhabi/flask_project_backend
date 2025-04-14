from flask import request, jsonify
from app.core.services.CategoryService import CategoryService


class CategoryController:
    def __init__(self):
        self.service = CategoryService()

    def get_categories(self):
        categories = self.service.get_all_categories()
        return jsonify([category.to_dict() for category in categories])

    def create_category(self):
        data = request.get_json()
        new_category = self.service.create_category(data)
        return jsonify(new_category.to_dict()), 201


