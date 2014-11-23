from aikithoughts.blueprints.main import main_blueprint


@main_blueprint.route('/')
def index():
    return "Hello World!"