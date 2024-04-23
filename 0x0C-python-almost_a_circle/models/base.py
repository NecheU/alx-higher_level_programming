#!/usr/bin/python3
"""Python_Alomst_A_Circle
Defining my ClassBase file
"""


class Base:
    """My Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
