from flask.blueprints import Blueprint

account_blueprint = Blueprint('account', __name__)

from . import account