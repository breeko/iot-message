import yaml

CONFIG = "../config.yml"

def load_config():
    with open(CONFIG, 'r') as stream:
        return yaml.safe_load(stream)