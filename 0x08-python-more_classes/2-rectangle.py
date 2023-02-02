#!/usr/bin/python3
"""This is the ``Rectangle`` module"""


class Rectangle:
    """The Rectangle class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize an instance of the Rectangle class.
            Args:
                width (int): The width of the rectangle
                height (int): The height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the witdh of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the permeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
