from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)  # manages configs

db = SQLAlchemy(app)  # the database
migrate = Migrate(app, db)  # database upgrades and stuff

login = LoginManager(app)  # manages logins
login.login_view = 'login'

from app import routes, models

# routes blueprint way but idk how
# from routes import *
# app.register_blueprint(routes)
