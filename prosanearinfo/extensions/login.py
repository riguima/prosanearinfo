from flask_login import LoginManager

from prosanearinfo.database import Session
from prosanearinfo.models import User


def init_app(app):
    login_manager = LoginManager()
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        with Session() as session:
            return session.get(User, int(user_id))

    login_manager.init_app(app)
