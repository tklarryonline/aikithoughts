import os
from flask.ext.security.datastore import SQLAlchemyUserDatastore
from flask.templating import render_template

from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.blueprints.main import main_blueprint
from aikithoughts.runtime import app, csrf, db, security
from aikithoughts import models


def create_app():
    # Registers configurations
    app.config.from_object(os.environ.get('APP_SETTINGS', 'config.common.LocalConfig'))

    # Enables CSRF protection
    csrf.init_app(app)

    _setup_blueprints(app)

    # Setups database
    db.init_app(app)

    # Setups
    _setup_security(app)

    _setup_errorhandlers(app)

    return app


def _setup_blueprints(app):
    # Registers blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(account_blueprint, url_prefix='/account')


def _setup_security(app):
    user_datastore = SQLAlchemyUserDatastore(db, models.accounts.User, models.authentications.Role)
    security.init_app(app, user_datastore)


def _setup_errorhandlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('main/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        db.session.rollback()
        return render_template('main/500.html'), 500
