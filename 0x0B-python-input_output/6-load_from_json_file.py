#!/usr/bin/python3
"""
Python Input and Output
Funtion to creat an object from JSON file
"""


def load_from_json_file(filename):
    """Func to create an obj from JSON file"""
    with open(filename, 'r') as file:
        v = json.load(file)
        return v
