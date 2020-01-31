#!/usr/bin/python3
"""Module of rectangle"""


from models.base import Base


class Rectangle(Base):
        """ class of Rectangle """

        def __init__(self, width, height, x=0, y=0, id=None):
            """ initializing the Rectangle """

            super().__init__(id)
            self.width = width
            self.height = height
            self.x = x
            self.y = y

        @property
        def width(self):
            """ width getter """

            return self.__width

        @width.setter
        def width(self, value):
            """ width setter """

            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):

            """ height getter """
            return self.__height

        @height.setter
        def height(self, value):

            """ height setter """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """ x getter """

            return self.__x

        @x.setter
        def x(self, value):
            """ x setter """

            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """ y getter """

            return self.__y

        @y.setter
        def y(self, value):
            """ y setter """

            if not isinstance(value, int):
                raise ValueError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """ area of the rectangle """

            return (self.width * self.height)

        def display(self):
            """ display the rectangle """

            for n in range(0, self.y):
                print()
            for i in range(0, self.height):
                for l in range(0, self.x):
                    print(" ", end="")
                for j in range(0, self.width):
                    print('#', end='')
                print()

        def __str__(self):
            """ string of the class """

            return ("[Rectangle] ({}) {}/{} - {}/{}".
                    format(self.id, self.x, self.y, self.width, self.height))

        def update(self, *args, **kwargs):
            """ Update rectangle """

            length = len(args)
            if length >= 1:
                Base().__init__(args[0])
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length == 5:
                self.y = args[4]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

        def to_dictionary(self):
                """the dictionary representation of a Rectangle"""
                recdic = {}
                recdic["id"] = self.id
                recdic["width"] = self.width
                recdic["height"] = self.height
                recdic["x"] = self.x
                recdic["y"] = self.y
                return recdic
