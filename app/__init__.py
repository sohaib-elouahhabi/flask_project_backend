from flask import Flask
from app.core.routes.routes import register_routes
from app.bootstrap import setup_extensions, setup_config

def create_app():
    app = Flask(__name__)
    setup_config(app)
    setup_extensions(app)
    register_routes(app)
    return app
