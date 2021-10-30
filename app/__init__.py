from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# routes blueprint way but idk how
# from routes import *
# app.register_blueprint(routes)
