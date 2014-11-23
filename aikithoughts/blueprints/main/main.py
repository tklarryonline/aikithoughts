from flask.templating import render_template
from aikithoughts.blueprints.main import main_blueprint


@main_blueprint.route('/')
def index():
    return render_template('index.html')