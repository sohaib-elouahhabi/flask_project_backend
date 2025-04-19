from app.core.library.routes.category_routes import categories_routes
from app.core.library.routes.book_routes import books_routes


def register_routes(app):
    categories_routes(app)
    books_routes(app)
