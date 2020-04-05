#!/usr/bin/python3
"""
Public instance method print_stored() print the sorted list
"""


class MyList(list):
    """
    Parentclass MyList Childclass list
    """
    def print_sorted(self):
        print(sorted(self))
