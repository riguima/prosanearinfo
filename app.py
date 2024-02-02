from flask import Flask
from flask_cors import CORS
from importlib import import_module

from prosanearinfo.config import get_config


def load_extensions(app):
    for extension in get_config(app)['extensions']:
        extension_module = import_module(extension)
        extension_module.init_app(app)


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    CORS(app)
    load_extensions(app)
    return app


app = create_app()
