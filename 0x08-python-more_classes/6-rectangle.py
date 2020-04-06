#!/usr/bin/python3


class Rectangle:
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width) * (self.__height)

    def perimeter(self):
            return (self.__width + self.__height) * 2
    def __str__(self):
        string = ""
        for i in range(0, self.__height):
            for n in range(0, self.__width):
                string += '#'
                return string
    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))
    def __del__(self):
        print("Bye rectangle...")
