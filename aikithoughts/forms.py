from flask.ext.wtf.form import Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from aikithoughts.models.accounts import User


class EditProfileForm(Form):
    DUPLICATED_NICKNAME = 'This nickname is already been using'

    nickname = StringField(label='nickname', validators=[DataRequired()])
    about_me = TextAreaField(label='about me', validators=[Length(min=0, max=140)])
    submit = SubmitField()

    def __init__(self, original_nickname=None, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_nickname = original_nickname

    def validate_nickname(self, field):
        if self.original_nickname and field.data == self.original_nickname:
            return True

        user = User.query.filter_by(nickname=field.data).first()
        if user is not None:
            field.errors.append(self.DUPLICATED_NICKNAME)
            return False

        return True
