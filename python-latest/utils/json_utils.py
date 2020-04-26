import json
from json.decoder import JSONDecodeError


def parse_json(json_data):
    try:
        j = json.loads(json_data)
    except JSONDecodeError as ex:
        print("ERROR: Json decode error")
        j = None
    return j


def return_data():
    return j[node]
