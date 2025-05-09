from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt

def authorize(required_role,refresh=False):
    def decorator(fn):
        @wraps(fn)
        @jwt_required(refresh=refresh)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role")

            if not user_role:
                return jsonify({"msg": "Missing role in token"}), 400

            if user_role != required_role.value:
                return jsonify({
                    "msg": f"Access forbidden: required role '{required_role.value}', but got '{user_role}'"
                }), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
