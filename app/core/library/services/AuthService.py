from app.models.User import User
from passlib.hash import bcrypt
from app.bootstrap import db
from datetime import datetime
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity, get_jwt


class AuthService:
    def login(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if not user:
            return None, "User not found"

        if not bcrypt.verify(password, user.password):
            return None, "Invalid credentials"
        
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        additional_claims = {
            "role": user.role.value,
            "user_id": user.id
            }

        access_token = create_access_token(identity=
            user.username,
            additional_claims=additional_claims
            )
        
        refresh_token = create_refresh_token(
            identity=user.username,
            additional_claims=additional_claims
        )
        return user, {
            "access_token": access_token, 
            "refresh_token": refresh_token
            }

    def register(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(username=username).first():
            return None, "Username already taken"

        if User.query.filter_by(email=email).first():
            return None, "Email already registered"

        hashed_password = bcrypt.hash(password)
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return new_user, None
    
    def refresh_access_token(self):
        identity = get_jwt_identity()
        claims = get_jwt()

        access_token = create_access_token(
            identity=identity,
            additional_claims={
                "role": claims["role"],
                "user_id": claims["user_id"]
            }
        )
        return access_token

    def logout(self):
        identity = get_jwt_identity()
        user = User.query.filter_by(username=identity).first()

        if user:
            user.last_logged_out = datetime.now()
            db.session.commit()
        
        return True