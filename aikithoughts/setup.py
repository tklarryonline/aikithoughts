import os

from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.blueprints.main import main_blueprint
from aikithoughts.runtime import app, csrf, db


def setup():
    # Registers configurations
    app.config.from_object(os.environ.get('APP_SETTINGS'))

    # Enables CSRF protection
    csrf.init_app(app)

    _setup_blueprints(app)

    # Setups database
    db.init_app(app)

    return app


def _setup_blueprints(app):
    # Registers blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(account_blueprint, url_prefix='/account')
