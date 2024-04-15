#!/usr/bin/python3
"""
Python program to add a new attribute to an object
Function: def add_attribute(obj, name, value)
Args:
    obj: Object that a new attribute will be addes to
    name: name of the attribute
    vakue: Vakue of the attribute
Raise:
    TypeError: If new attribute cant be added to rhe object
"""


def add_attribute(object, name, value):
    if hasattr(object, '__dict__'):
        object.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
