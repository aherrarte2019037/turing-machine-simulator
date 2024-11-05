import yaml

def parse_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)
