import pytest
from unittest.mock import Mock, patch
from app.core.library.services.CategoryService import CategoryService
from app.models.Category import Category

class TestCategoryService:

    @pytest.fixture
    def category_service(self):
        return CategoryService()

    @patch('app.core.library.services.CategoryService.Category.query')
    def test_get_all_categories(self, mock_query, category_service, test_app):
        # Create a list of mock categories
        mock_categories = [
            Mock(spec=Category, id=1, name="Category 1"),
            Mock(spec=Category, id=2, name="Category 2"),
            Mock(spec=Category, id=3, name="Category 3")
        ]
        # Set up the mock query.all() to return our list of categories
        mock_query.all.return_value = mock_categories
        # Call the method being tested
        result = category_service.get_all_categories()
        # Verify the query was called correctly
        mock_query.all.assert_called_once()
        # Verify the result is what we expect
        assert result == mock_categories
        assert len(result) == 3 

    @patch('app.core.library.services.CategoryService.Category.query')
    def test_get_paginated_categories(self, mock_query, category_service, test_app):
        # Arrange
        mock_paginated_result = Mock()
        mock_paginated_result.items = [
            Mock(spec=Category, id=1, name="Cat 1"),
            Mock(spec=Category, id=2, name="Cat 2")
        ]
        mock_query.paginate.return_value = mock_paginated_result

        # Act
        result = category_service.get_paginated_categories(page=1, per_page=2)

        # Assert
        mock_query.paginate.assert_called_once_with(page=1, per_page=2, error_out=False)
        assert result.items == mock_paginated_result.items
        assert len(result.items) == 2 

    @patch('app.core.library.services.CategoryService.db.session')
    @patch('app.core.library.services.CategoryService.Category')
    def test_create_category(self, mock_category_class, mock_session, category_service, test_app):
        # Arrange
        data = {"name": "Test Category", "description": "Test Category"}
        mock_category_instance = Mock()
        mock_category_class.return_value = mock_category_instance

        # Act
        result = category_service.create_category(data)

        # Assert
        mock_category_class.assert_called_once_with(**data)
        mock_session.add.assert_called_once_with(mock_category_instance)
        mock_session.commit.assert_called_once()
        
        assert result == mock_category_instance

    @patch('app.core.library.services.CategoryService.Category.query')
    def test_get_category_by_id(self, mock_query, category_service, test_app):
        # Arrange
        mock_category = Mock(spec=Category)
        mock_query.get.return_value = mock_category
        
        # Act
        result = category_service.get_category_by_id(1)
        
        # Assert
        mock_query.get.assert_called_once_with(1)
        assert result == mock_category
    
    @patch('app.core.library.services.CategoryService.Category.query')
    @patch('app.core.library.services.CategoryService.db.session')
    def test_update_category(self, mock_session, mock_query, category_service, test_app):
        # Arrange
        mock_category = Mock(spec=Category)
        mock_category.id = 1
        mock_category.name = "Old Category"
        mock_category.description = "Old Description"
        
        mock_query.get.return_value = mock_category

        # Data to update the category
        update_data = {"name": "Updated Category", "description": "Updated Description"}

        # Act
        result = category_service.update_category(1, update_data)

        # Assert
        mock_query.get.assert_called_once_with(1)
        mock_session.commit.assert_called_once()

        # Verify the attributes were updated
        assert result.name == "Updated Category" 
        assert result.description == "Updated Description" 

    @patch('app.core.library.services.CategoryService.Category.query')
    @patch('app.core.library.services.CategoryService.db.session')
    def test_update_category_not_found(self, mock_session, mock_query, category_service, test_app):
        # Arrange
        mock_query.get.return_value = None

        update_data = {"name": "Updated Category", "description": "Updated Description"}

        # Act
        result = category_service.update_category(1, update_data)

        # Assert
        assert result is None
        mock_query.get.assert_called_once_with(1)
        mock_session.commit.assert_not_called() 


    @patch('app.core.library.services.CategoryService.Category.query')
    @patch('app.core.library.services.CategoryService.db.session')
    def test_delete_category(self, mock_session, mock_query, category_service, test_app):
        # Arrange
        mock_category = Mock(spec=Category)
        mock_category.id = 1
        mock_query.get.return_value = mock_category

        # Act
        result = category_service.delete_category(1)

        # Assert
        mock_query.get.assert_called_once_with(1)
        mock_session.delete.assert_called_once_with(mock_category)
        mock_session.commit.assert_called_once()
        assert result == mock_category

    @patch('app.core.library.services.CategoryService.Category.query')
    @patch('app.core.library.services.CategoryService.db.session')
    def test_delete_category_not_found(self, mock_session, mock_query, category_service, test_app):
        # Arrange
        mock_query.get.return_value = None 

        # Act
        result = category_service.delete_category(1)
        
        # Assert
        assert result is None
        mock_query.get.assert_called_once_with(1) 
        mock_session.delete.assert_not_called()
        mock_session.commit.assert_not_called() 