from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError


def validate_request(model_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400
            try:
                validated_data = model_class.model_validate(data)
                return func(*args, validated_data=validated_data, **kwargs)
            except ValidationError as e:
                errors = [{
                    'field': ".".join(str(loc) for loc in err['loc']),
                    'message': err['msg'],
                    'type': err['type']
                } for err in e.errors()]
                return jsonify({"errors": errors}), 400
        return wrapper
    return decorator