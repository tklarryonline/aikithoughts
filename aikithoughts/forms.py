from flask.ext.wtf.form import Form
from wtforms.fields.core import StringField, BooleanField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired


class LoginOpenIDForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Sign in')