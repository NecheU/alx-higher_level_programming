#!/usr/bin/python3
"""Pytjon Input and Output
Concerting json strings to python
"""


import json
def from_json_string(my_str):
    """Func to convert json to python"""
    return json.load(my_str)
