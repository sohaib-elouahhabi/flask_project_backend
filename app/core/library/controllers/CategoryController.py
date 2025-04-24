from flask import request, jsonify
from app.core.library.services.CategoryService import CategoryService
from app.core.library.requests.CategoryRequestModel import CategoryRequestModel
from pydantic import ValidationError


class CategoryController:
    def __init__(self):
        self.service = CategoryService()
    
    def get_categories(self):
        # Get pagination parameters from the request
        page = request.args.get('page', 1, type=int)  # Default to page 1
        per_page = request.args.get('per_page',5, type=int)  

        # Fetch paginated categories from the service
        paginated_categories = self.service.get_paginated_categories(page, per_page)

        # Prepare the response
        return jsonify({
            "categories": [category.to_dict() for category in paginated_categories.items],
            "total": paginated_categories.total,
            "page": paginated_categories.page,
            "per_page": paginated_categories.per_page,
            "pages": paginated_categories.pages
        })

    def create_category(self):
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        try:
            category_data = CategoryRequestModel.model_validate(data)
            
           
            new_category = self.service.create_category(category_data.model_dump())
            
            return jsonify(new_category.to_dict()), 201
            
        except ValidationError as e:
            # Format Pydantic errors for better client response
            errors = []
            for error in e.errors():
                field = ".".join(str(loc) for loc in error['loc'])
                errors.append({
                    'field': field,
                    'message': error['msg'],
                    'type': error['type']
                })
            return jsonify({"errors": errors}), 400
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def get_category_by_id(self, category_id):
        category = self.service.get_category_by_id(category_id)
        if category:
            return jsonify(category.to_dict())
        return jsonify({"error": "Category not found"}), 404
    
    def update_category(self, category_id):
        data = request.get_json()
        try:
        
            category_data = CategoryRequestModel(**data)  
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400
        category_data_dict = category_data.model_dump()
        updated_category = self.service.update_category(category_id, category_data_dict)
        if updated_category:
            return jsonify(updated_category.to_dict()), 200
        return jsonify({"error": "Category not found"}), 404
    
    def delete_category(self, category_id):
        deleted_category = self.service.delete_category(category_id)
        if deleted_category:
            return jsonify(deleted_category.to_dict())
        return jsonify({"error": "Category not found"}), 404
    
    
    


