from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.blueprints.main import main_blueprint
from aikithoughts.runtime import app, csrf


def setup():
    # Registers configurations
    app.config.from_object('config.common')
    app.config.from_object('config.local')

    # Enable CSRF protection
    csrf.init_app(app)

    _setup_blueprints(app)


def _setup_blueprints(app):
    # Registers blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(account_blueprint, url_prefix='/account')
