from flask import Flask
from flask_cors import CORS
from app.core.library.routes.routes import register_routes
from app.bootstrap import setup_extensions, setup_config

def create_app():
    app = Flask(__name__)
    setup_config(app)
    setup_extensions(app)
    register_routes(app)
    CORS(app)
    return app
