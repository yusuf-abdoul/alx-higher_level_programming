#!/usr/bin/python3
"""The ``MyList`` module"""


class MyList(list):
    """MyList inheriting from the ``list`` class"""

    def print_sorted(self):
        """ Method that prints the sorted list """
        print(sorted(self))
