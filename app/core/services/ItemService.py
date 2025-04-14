from app.core.models.Item import Item
from app.bootstrap import db

class ItemService:
    def get_all_items(self):
        return Item.query.all()

    def create_item(self, data):
        item = Item(**data)
        db.session.add(item)
        db.session.commit()
        return item
    
    def get_item_by_id(self, item_id):
        return Item.query.get(item_id)
    
    def get_items_by_category(self, category_id):
        return Item.query.filter_by(category_id=category_id).all()
    
    
    def update_item(self, item_id, data):
        item = self.get_item_by_id(item_id)
        if item:
            for key, value in data.items():
                setattr(item, key, value)
            db.session.commit()
            return item
        return None
    
    def delete_item(self, item_id):
        item = self.get_item_by_id(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
    
    
