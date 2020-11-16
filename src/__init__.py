from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from src.config import Config

# Binding Extentions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.sign_in'
login_manager.login_message_category = 'info',
mail = Mail()


def create_app(config_class=Config):
    # Initializing the flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initializing Extensions for the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from src.main.routes import main
    from src.users.routes import users
    from src.posts.routes import posts

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    return app