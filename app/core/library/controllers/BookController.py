from flask import request, jsonify
from app.core.library.services.BookService import BookService


class BookController:
    def __init__(self):
        self.service = BookService()

    def get_books(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 3, type=int)

        books_paginated = self.service.get_books_paginated(page, per_page)

        return jsonify({
            'total': books_paginated.total,
            'pages': books_paginated.pages,
            'current_page': books_paginated.page,
            'per_page': books_paginated.per_page,
            'items': [book.to_dict() for book in books_paginated.items]
        })
    
    def get_book_by_id(self, book_id):
        book = self.service.get_book_by_id(book_id)
        if book:
            return jsonify(book.to_dict())
        return jsonify({"error": "Book not found"}), 404
    
    def get_books_by_category(self, category_id):
        books = self.service.get_books_by_category(category_id)
        return jsonify([book.to_dict() for book in books])

    def create_book(self):
        data = request.get_json()
        new_book = self.service.create_book(data)
        return jsonify(new_book.to_dict()), 201

    def update_book(self, book_id):
        data = request.get_json()
        updated_book = self.service.update_book(book_id, data)
        if updated_book:
            return jsonify(updated_book.to_dict())
        return jsonify({"error": "Book not found"}), 404

    def delete_book(self, book_id):
        deleted_book = self.service.delete_book(book_id)
        if deleted_book:
            return jsonify(deleted_book.to_dict())
        return jsonify({"error": "Book not found"}), 404
    