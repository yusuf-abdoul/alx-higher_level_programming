#!/usr/bin/python3
# 1-rectangle.py

"""This is a module composed of a class that defines a Rectangle"""


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
        """ method that returns the value of the width

	Returns:
	the width of the rectangle

	"""
        return self.__width

    @width.setter
    def width(self, value):
        """ method that set the witdh of the rectangle

	Args:
		value: width
	Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

	Set the witdh of the rectangle

	"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that set the height of the rectangle

	Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

	"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
