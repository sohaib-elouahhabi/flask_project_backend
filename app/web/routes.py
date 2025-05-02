from app.web.book.BookController import books_routes
from app.web.category.CategoryController import categories_routes

def register_routes(app):
    books_routes(app)
    categories_routes(app)