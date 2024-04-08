#!/usr/bin/python3
"""class Rectangle based on 0-rectangle.py
Private instance attribute:
    width:
    heigth:
if width is less than 0:
raise a ValueError exception with the message width must be >= 0

if height is less than 0:
raise a ValueError exception with the message height must be >= 0
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            if value < 0:
                raise ValueError("Width must be >= 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
