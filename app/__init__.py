from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.web.routes import register_routes
from app.bootstrap import setup_extensions, setup_config
from datetime import timedelta


def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = '80a99bb862112af114f20af5ed9723c1a33d021777234eae82a4b319079ddf32'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)  
    jwt = JWTManager(app)

    setup_config(app)
    setup_extensions(app)
    register_routes(app)
    CORS(app)
    return app
