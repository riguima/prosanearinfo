from flask import current_app
import toml


def get_config(app=None):
    app = app or current_app
    config = toml.load(open('.config.toml', 'r'))
    return config['testing'] if app.config['TESTING'] else config['default']
