from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def setup_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def setup_config(app):
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@localhost/flask_db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
