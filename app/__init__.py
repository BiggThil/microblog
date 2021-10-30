from flask import Flask

app = Flask(__name__)

from app import routes

# routes blueprint way but idk how
# from routes import *
# app.register_blueprint(routes)
