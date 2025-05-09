from app.bootstrap import db
from sqlalchemy import Enum as SqlEnum 
from app.models.UserRole import UserRole
from datetime import datetime
from .AuditMixin import AuditMixin

class User(AuditMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(SqlEnum(UserRole), nullable=False, default=UserRole.USER)
    last_login = db.Column(db.DateTime, nullable=True)
    last_logged_out = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role.name,
        }