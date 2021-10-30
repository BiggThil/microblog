from flask import render_template
from . import routes

@routes.route('/')
@routes.route('/index')
def index():
  return "hewwo world"
