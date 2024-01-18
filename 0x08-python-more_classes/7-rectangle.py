#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """ Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init method """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Str"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rep = ""
        for i in range(self.__height):
            rep += Rectangle.print_symbol * self.__width + '\n'
        return rep[:-1]

    def __repr__(self):
        """Repr"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """"Del"""
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
