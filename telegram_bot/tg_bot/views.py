from flask import Blueprint

shopping_list_bp = Blueprint('shopping_list', __name__)


@shopping_list_bp.route('/')
def index():
    return 'Welcome to the Shopping List Bot!'

