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
    if isinstance(object, str):
        raise TypeError("can't add a new attribute")
    setattr(object, name, value)
    if not hasattr(object, name):
        raise TypeError("can't add a new attribute")
