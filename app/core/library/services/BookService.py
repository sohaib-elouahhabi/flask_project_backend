from app.core.models.Book import Book
from app.bootstrap import db


class BookService:
    def get_all_books(self):
        return Book.query.all()
    
    def get_books_paginated(self, page, per_page):
        return Book.query.paginate(page=page, per_page=per_page, error_out=False)
    
    def get_book_by_id(self, book_id):
        return Book.query.get(book_id)
    
    def get_books_by_category(self, category_id):
        return Book.query.filter_by(category_id=category_id).all()
    
    def get_books_by_author(self, author):
        return Book.query.filter_by(author=author).all()
    
    def create_book(self, data):
        book = Book(**data)
        db.session.add(book)
        db.session.commit()
        return book

    def update_book(self, book_id, data):
        book = Book.query.get(book_id)
        if not book:
            return None
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return book

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return None
        db.session.delete(book)
        db.session.commit()
        return book