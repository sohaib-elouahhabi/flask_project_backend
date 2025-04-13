from app.core.models.Category import Category
from app.bootstrap import db


class CategoryService:
    def get_all_categories(self):
        return Category.query.all()

    def create_category(self, data):
        category = Category(**data)
        db.session.add(category)
        db.session.commit()
        return category
