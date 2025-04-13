from app.core.routes.item_routes import items_routes 
from app.core.routes.category_routes import categories_routes


def register_routes(app):
    items_routes(app)
    categories_routes(app)
