from flask import Blueprint, request, jsonify
from app.core.library.services.BookService import BookService
from app.web.requests.BookRequestModel import BookRequestModel
from app.core.common.utils.validation import validate_request

# Create the blueprint instance
book_blueprint = Blueprint('book', __name__)

# Initialize the BookService
service = BookService()

# Define the route for getting books
@book_blueprint.route('/', methods=['GET'])
def get_books():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    books_paginated = service.get_books_paginated(page, per_page)

    return jsonify({
        'total': books_paginated.total,
        'pages': books_paginated.pages,
        'current_page': books_paginated.page,
        'per_page': books_paginated.per_page,
        'items': [book.to_dict() for book in books_paginated.items]
    })

# Define the route for getting a book by ID
@book_blueprint.route('/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = service.get_book_by_id(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404

# Define the route for getting books by category
@book_blueprint.route('/category/<int:category_id>', methods=['GET'])
def get_books_by_category(category_id):
    books = service.get_books_by_category(category_id)
    return jsonify([book.to_dict() for book in books])

# Define the route for creating a new book
@book_blueprint.route('/', methods=['POST'])
@validate_request(BookRequestModel)
def create_book(validated_data):
    new_book = service.create_book(validated_data.model_dump())
    return jsonify(new_book.to_dict()), 201

# Define the route for updating an existing book
@book_blueprint.route('/<int:book_id>', methods=['PUT'])
@validate_request(BookRequestModel)
def update_book(book_id, validated_data):
    updated_book = service.update_book(book_id, validated_data.model_dump())
    if updated_book:
        return jsonify(updated_book.to_dict()), 200
    return jsonify({"error": "Book not found"}), 404

# Define the route for deleting a book
@book_blueprint.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    deleted_book = service.delete_book(book_id)
    if deleted_book:
        return jsonify(deleted_book.to_dict())
    return jsonify({"error": "Book not found"}), 404

# Method to register the blueprint with the app
def books_routes(app):
    app.register_blueprint(book_blueprint, url_prefix='/api/v1/books')
