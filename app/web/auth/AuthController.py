from flask import Blueprint, request, jsonify, make_response
from app.core.library.services.AuthService import AuthService
from app.web.common.utils.validation import validate_request
from flask_jwt_extended import set_refresh_cookies, unset_jwt_cookies, jwt_required
from app.web.requests.AuthRequestModel import LoginRequestModel, RegisterRequestModel


auth_blueprint = Blueprint('user', __name__)
service = AuthService()

@auth_blueprint.route('/login', methods=['POST'])
@validate_request(LoginRequestModel)
def login(validated_data):
    user, tokens = service.login(validated_data.model_dump())

    if not user:
        return jsonify({"error": tokens}), 401

    response = make_response(jsonify({
        "message": "Login successful",
        "access_token": tokens["access_token"],
        "user": {
            "id": user.id,
            "username": user.username
        }
    }))
    set_refresh_cookies(response, tokens["refresh_token"])
    return response, 200
    # return redirect(url_for('category.get_categories'))
    

@auth_blueprint.route('/register', methods=['POST'])
@validate_request(RegisterRequestModel)
def register(validated_data):
    user, error = service.register(validated_data.model_dump())

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "username": user.username
        }
    }), 201

@auth_blueprint.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    new_token = service.refresh_access_token()
    return jsonify({"access_token": new_token}), 200

@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    service.logout()
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200
    
def auth_routes(app):
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1')
