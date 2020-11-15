import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5e0e3c55977f326856efa3530e903d9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pyblog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in'
login_manager.login_message_category = 'info'
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USER_TLS'] = True
# # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
# app.config['MAIL_USERNAME'] = 'ogungburedamilola@gmail.com'
# app.config['MAIL_PASSWORD'] = 'd1a2m3i4.,'

app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'cb92231b21b23f'
app.config['MAIL_PASSWORD'] = '66ee86986c3a2a'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
from src import routes