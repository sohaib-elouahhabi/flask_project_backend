from app.models.Category import Category
from app.bootstrap import db


class CategoryService:
    def get_all_categories(self):
        return Category.not_deleted().all()
    
    def get_paginated_categories(self, page, per_page):
        return Category.not_deleted().paginate(page=page, per_page=per_page, error_out=False)

    def create_category(self, data):
        category = Category(**data)
        db.session.add(category)
        db.session.commit()
        return category
    
    def get_category_by_id(self, category_id):
        return Category.query.get(category_id)
    
    def update_category(self, category_id, data):
        category = Category.query.get(category_id)
        if not category:
            return None
        for key, value in data.items():
            setattr(category, key, value)
        db.session.commit()
        return category
    
    def delete_category(self, category_id):
        category = Category.query.get(category_id)
        if not category:
            return None
        category.soft_delete()
        return category
    
