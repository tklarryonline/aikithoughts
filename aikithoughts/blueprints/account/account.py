from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.forms import LoginOpenIDForm


@account_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginOpenIDForm()

    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect(url_for('main.index'))

    return render_template('account/login.html', form=form)