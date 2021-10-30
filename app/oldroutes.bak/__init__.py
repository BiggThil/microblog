from flask import Blueprint
routes = Blueprint('routes', __name__)

# routes imports (from .index import *)
from .index import *

