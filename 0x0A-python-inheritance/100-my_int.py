#!/usr/bin/python3

class MyInt(int):
    """class MyInt inherits int"""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return super().__eq__(other)
