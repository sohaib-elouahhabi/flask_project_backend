from app.bootstrap import db
from .AuditMixin import AuditMixin

class Book(AuditMixin):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    category = db.relationship('Category', back_populates='books')
    
    def to_dict(self):
        return {
                'id': self.id,
                'title': self.title,
                'author': self.author,
                'published_date': self.published_date,
                'category_id': self.category_id, 
            }