import json

def get_all_operations(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)