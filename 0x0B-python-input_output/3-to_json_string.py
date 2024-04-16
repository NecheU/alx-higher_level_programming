#!/usr/bin/python3
"""Python Input and Output
Python function that returns json representation
"""


def to_json_string(my_obj):
    """Func that returns JSON rep of obj str"""
    if isinstance(my_obj, str):
        return f'"{my_obj}"'
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, list):
        return '[' + ', '.join(to_json_string(item) for item in my_obj) + ']'
    elif isinstance(my_obj, dict):
        return '{' + ', '.join(f'"{key}": {to_json_string(value)}' for key, value in my_obj.item()) + '}'
    else:
        return None
