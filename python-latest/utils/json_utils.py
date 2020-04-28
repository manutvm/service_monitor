import json
from json.decoder import JSONDecodeError


def parse_json_data(json_data):
    try:
        j = json.loads(json_data)
    except JSONDecodeError as ex:
        print("ERROR: Json decode error")
        j = None
    return j

def parse_json_file(json_data):
    try:
        j = json.load(json_data)
    except JSONDecodeError as ex:
        print("ERROR: Json decode error")
        j = None
    return j

def return_data():
    return j[node]
