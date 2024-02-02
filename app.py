from importlib import import_module

from flask import Flask

from prosanearinfo.config import get_config


def load_extensions(app):
    for extension in get_config()['extensions']:
        extension_module = import_module(extension)
        extension_module.init_app(app)


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.update(
        {
            'SECRET_KEY': get_config()['secret_key'],
        }
    )
    load_extensions(app)
    return app


app = create_app()
