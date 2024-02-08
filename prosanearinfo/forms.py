from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])


class ConfigForm(FlaskForm):
    pix = StringField('Pix', validators=[DataRequired()])
