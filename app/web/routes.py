from app.web.book.BookController import books_routes
from app.web.category.CategoryController import categories_routes
from app.web.auth.AuthController import auth_routes

def register_routes(app):
    books_routes(app)
    categories_routes(app)
    auth_routes(app)