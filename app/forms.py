from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import Form


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
