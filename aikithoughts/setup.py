from aikithoughts.blueprints.main import main_blueprint
from aikithoughts.runtime import app


def setup():
    # Registers blueprints
    app.register_blueprint(main_blueprint)