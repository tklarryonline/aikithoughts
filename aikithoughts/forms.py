from flask.ext.wtf.form import Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class EditProfileForm(Form):
    nickname = StringField(label='nickname', validators=[DataRequired()])
    about_me = TextAreaField(label='about me', validators=[Length(min=0, max=140)])
    submit = SubmitField()
