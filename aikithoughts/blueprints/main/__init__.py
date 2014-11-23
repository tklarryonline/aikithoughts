from flask.blueprints import Blueprint

main_blueprint = Blueprint('main', __name__)

from . import main