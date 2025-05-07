from app.models.User import User
from passlib.hash import bcrypt
from app.bootstrap import db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import decode_token


class AuthService:
    def login(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if not user:
            return None, "User not found"

        if not bcrypt.verify(password, user.password):
            return None, "Invalid credentials"
        additional_claims = {"role": user.role.value,'user_id': user.id}
        access_token = create_access_token(identity=
            user.username,
            additional_claims=additional_claims
            )
        return user, access_token
    
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