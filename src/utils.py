import yaml

def load_config(config):
    with open(config, 'r') as stream:
        return yaml.safe_load(stream)