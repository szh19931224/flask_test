from flask import Blueprint

helloworld_bp = Blueprint('helloworld', __name__)

from . import helloworld



