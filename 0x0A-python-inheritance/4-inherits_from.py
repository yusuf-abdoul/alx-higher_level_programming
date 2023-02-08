#!/usr/bin/python3
""" The ``inherits_from`` module"""

def inherits_from(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """

	return type(obj) is not a_class and isinstance(obj, a_class)
