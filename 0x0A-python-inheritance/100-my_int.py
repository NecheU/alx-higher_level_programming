#!/usr/bin/python3
"""Python Inheritance:
    Class: Myint
    Inherited from the inbuilt int clas
"""


class MyInt(int):
    """class MyInt inherits int"""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return super().__eq__(other)
