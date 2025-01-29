from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
import secrets

db = SQLAlchemy()
migrate = Migrate()
print("david and dana")
def create_app():
    app = Flask(__name__, static_folder='static')    
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from .routes import init_apps
    init_apps(app) 
    return app
