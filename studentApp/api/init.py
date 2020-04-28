from django import Blueprint

api = Blueprint("api", __name__)

from . import views