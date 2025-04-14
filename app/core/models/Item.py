from app.bootstrap import db 

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    category = db.relationship('Category', back_populates='items')
    
    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'price': self.price,
                'category_id': self.category_id, 
            }
