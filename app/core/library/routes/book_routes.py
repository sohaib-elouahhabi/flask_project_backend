from flask import Blueprint
from app.core.library.controllers.BookController import BookController

mod = Blueprint('book', __name__, ) 
book_controller = BookController()

@mod.route('/', methods=['GET'])
def get_items():
    return book_controller.get_books()

@mod.route('/', methods=['POST'])
def create_item():
    return book_controller.create_book()

@mod.route('/<int:book_id>', methods=['GET'])
def get_item(book_id):
    return book_controller.get_book_by_id(book_id)

@mod.route('/<int:book_id>', methods=['PUT'])
def update_item(book_id):
    return book_controller.update_book(book_id)

@mod.route('/<int:book_id>', methods=['DELETE'])
def delete_item(book_id):
    return book_controller.delete_book(book_id)

@mod.route('/category/<int:category_id>', methods=['GET'])
def get_items_by_category(category_id):
    return book_controller.get_books_by_category(category_id)




def books_routes(app):
    app.register_blueprint(mod, url_prefix='/api/v1/books')
