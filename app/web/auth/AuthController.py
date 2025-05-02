from flask import Blueprint, request, jsonify
from app.core.library.services.AuthService import AuthService


auth_blueprint = Blueprint('user', __name__)
service = AuthService()

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user, access_token = service.login(data)
    
    if not user:
        return jsonify({"error": access_token}), 401

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username
        }
    }), 200
    # return redirect(url_for('category.get_categories'))
    

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user, error = service.register(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "username": user.username
        }
    }), 201

def auth_routes(app):
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1')
