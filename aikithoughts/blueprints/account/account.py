# -*- coding: utf-8 -*-
from flask.ext.login import login_required, current_user
from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect

from aikithoughts.blueprints.account import account_blueprint
from aikithoughts.forms import EditProfileForm
from aikithoughts.models.accounts import User
from aikithoughts.runtime import db


@account_blueprint.route('/profile/<id>')
@login_required
def profile(id):
    user = User.query.get(id)
    if user is None:
        flash(u'We can’t find this User %s :(' % id)
        return redirect(url_for('main.index'))

    return render_template('account/profile.html', user=user)


@account_blueprint.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(original_nickname=current_user.nickname, obj=current_user)

    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.add(current_user)
        db.session.commit()

        flash('Updated your info')
        return redirect(url_for('account.profile', id=current_user.id))

    return render_template('account/edit_profile.html', form=form)
