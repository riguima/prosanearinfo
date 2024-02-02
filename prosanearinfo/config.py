import toml


def get_config():
    return toml.load(open('.config.toml', 'r'))
