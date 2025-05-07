from flask import Blueprint, request, jsonify
from app.core.library.services.CategoryService import CategoryService
from app.web.requests.CategoryRequestModel import CategoryRequestModel
from app.web.common.utils.validation import validate_request
from flask_jwt_extended import jwt_required
from app.models.UserRole import UserRole
from app.web.common.authorization import authorize

# Create the blueprint instance
category_blueprint = Blueprint('category', __name__)

# Initialize the CategoryService
service = CategoryService()

# Define the route for getting categories
@category_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_categories():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    paginated_categories = service.get_paginated_categories(page, per_page)

    return jsonify({
        'total': paginated_categories.total,
        'pages': paginated_categories.pages,
        'current_page': paginated_categories.page,
        'per_page': paginated_categories.per_page,
        'items': [category.to_dict() for category in paginated_categories.items]
    })

# Define the route for getting a category by ID
@category_blueprint.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = service.get_category_by_id(category_id)
    if category:
        return jsonify(category.to_dict())
    return jsonify({"error": "Category not found"}), 404

# Define the route for creating a new category
@category_blueprint.route('/', methods=['POST'])
@authorize(UserRole.USER)
@validate_request(CategoryRequestModel)
def create_category(validated_data):
    new_category = service.create_category(validated_data.model_dump())
    return jsonify(new_category.to_dict()), 201

# Define the route for updating an existing category
@category_blueprint.route('/<int:category_id>', methods=['PUT'])
@validate_request(CategoryRequestModel)
def update_category(category_id, validated_data):
    updated_category = service.update_category(category_id, validated_data.model_dump())
    if updated_category:
        return jsonify(updated_category.to_dict()), 200
    return jsonify({"error": "Category not found"}), 404

# Define the route for deleting a category
@category_blueprint.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    deleted_category = service.delete_category(category_id)
    if deleted_category:
        return jsonify(deleted_category.to_dict())
    return jsonify({"error": "Category not found"}), 404

# Method to register the blueprint with the app
def categories_routes(app):
    app.register_blueprint(category_blueprint, url_prefix='/api/v1/categories')