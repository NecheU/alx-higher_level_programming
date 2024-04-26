#!/usr/bin/python3

"""Python_Almost_A_Circle
Class Rectangle that inherit
from class Base
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle inheritting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the wisth attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attr"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attr"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """Getter for x attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x attr"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Getter for y attr"""
        return self.__y

    @y.setter
    def y(value, int):
        """setter for y attr"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """Calc the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String rep of the rectangle"""
         return (f"[Rectangle] ({self.id}) - x: {self.x}, y: {self.y}, "
                 f"width: {self.width}, height: {self.height}")
