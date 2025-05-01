import pytest
from unittest.mock import Mock, patch
from app.core.library.services.BookService import BookService
from app.models.Book import Book


class TestBookService:

    @pytest.fixture
    def book_service(self):
        return BookService()

    @patch('app.core.library.services.BookService.Book.query')
    def test_get_book_by_id(self, mock_query, book_service, test_app):
        mock_book = Mock(spec=Book)
        mock_book.id = 1
        mock_book.title = "Test Book"
        mock_book.author = "Test Author"
        
        mock_query.get.return_value = mock_book
        
        result = book_service.get_book_by_id(1)
        
        mock_query.get.assert_called_once_with(1)
        
        assert result == mock_book
