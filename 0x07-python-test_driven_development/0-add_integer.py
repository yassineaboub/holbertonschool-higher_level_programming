#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The example module supplies one function, add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    addition = a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float and type(b) is float:
        if (a + b) == float("inf") or (a + b) == -float("inf"):
            raise ValueError("float overflow")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
