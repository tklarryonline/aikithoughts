from flask.templating import render_template
from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.forms import LoginOpenIDForm


@account_blueprint.route('/login/', methods=['GET'])
def login():
    form = LoginOpenIDForm()
    return render_template('account/login.html', form=form)