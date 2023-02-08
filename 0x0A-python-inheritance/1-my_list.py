#!/usr/bin/python3
"""The ``MyList`` module"""

class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        print(sorted(self))
