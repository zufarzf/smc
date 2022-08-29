from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from config import config

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
from . import models

def create_app(config_name):
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    from .main import main
    from .admin import admin
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix="/admin")

    return app