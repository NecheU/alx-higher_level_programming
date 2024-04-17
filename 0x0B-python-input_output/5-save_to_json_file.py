#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
