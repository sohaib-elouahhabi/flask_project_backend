from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, event
from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request,get_jwt
from flask import has_request_context

from app.bootstrap import db

class AuditMixin(db.Model):
    """Base model class that includes common fields and behaviors"""
    
    __abstract__ = True
    
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.now, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)
    
    @classmethod
    def __declare_last__(cls):
        """Register SQLAlchemy event listeners for the class"""
        event.listen(cls, 'before_insert', cls._before_insert)
        event.listen(cls, 'before_update', cls._before_update)
    
    @staticmethod
    def _before_insert(mapper, connection, target):
        """Set created_by and created_at before insert"""
        target.created_at = datetime.now()

        if has_request_context():
            try:
                verify_jwt_in_request() 
                current_user_id = get_jwt().get("user_id")
                if current_user_id:
                    target.created_by = current_user_id
            except Exception as e:
                print("JWT not available or invalid:", e)


    @staticmethod
    def _before_update(mapper, connection, target):
        """Update updated_by and updated_at before update"""
        target.updated_at = datetime.now()

        if has_request_context():
            try:
                verify_jwt_in_request()
                user_id = get_jwt().get("user_id")
                if user_id:
                    target.updated_by = user_id
            except Exception as e:
                print("JWT not available or invalid during update:", e)

    
    def soft_delete(self):
        self.deleted_at = datetime.now()
        if has_request_context():
            try:
                verify_jwt_in_request()
                user_id = get_jwt().get("user_id")
                if user_id:
                    self.deleted_by = user_id
                    print(user_id)
            except Exception as e:
                print("JWT not available during soft delete:", e)

        db.session.commit()

    @classmethod
    def not_deleted(cls):
        return cls.query.filter_by(deleted_at=None)