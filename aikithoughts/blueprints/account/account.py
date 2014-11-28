# -*- coding: utf-8 -*-
from flask.ext.login import login_required
from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect

from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.models.accounts import User


@account_blueprint.route('/profile/<id>')
@login_required
def profile(id):
    user = User.query.get(id)
    if user is None:
        flash(u'We can’t find this User %s :(' % id)
        return redirect(url_for('main.index'))

    return render_template('account/profile.html', user=user)