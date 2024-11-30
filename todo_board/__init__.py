from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import db_models

    from todo_board.views import main_view, todo_view, auth_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(todo_view.bp)
    app.register_blueprint(auth_view.bp)

    return app