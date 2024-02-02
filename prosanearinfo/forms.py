from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired

from prosanearinfo.config import config


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])


class ConfigForm(FlaskForm):
    name = StringField(
        'Nome',
        validators=[DataRequired()],
        render_kw={'value': config['name']},
    )
    city = StringField(
        'Cidade',
        validators=[DataRequired()],
        render_kw={'value': config['city']},
    )
    pix = StringField(
        'Pix', validators=[DataRequired()], render_kw={'value': config['pix']}
    )
    txt_id = StringField(
        'TXT ID',
        validators=[DataRequired()],
        render_kw={'value': config['txt_id']},
    )
