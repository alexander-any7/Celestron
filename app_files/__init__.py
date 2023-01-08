from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app_files.config import Config
from flask_share import Share


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
share = Share()


def create_app():
    config = Config
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    share.init_app(app)

    from app_files.index.routes import index
    from app_files.users.routes import users
    from app_files.posts.routes import posts
    from app_files.errors.handlers import errors

    app.register_blueprint(index)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
