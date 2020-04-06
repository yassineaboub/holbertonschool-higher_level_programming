#!/usr/bin/python3
"""
BaseGeometry module
"""


class BaseGeometry:
        """ Public instance method """
        def area(self):
            raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
            """ Public instance method validate values"""

            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
