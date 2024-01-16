#!/usr/bin/python3
"""Contains sqaure class """


class Square:
    """ Square class"""
    def __init__(self, size=0):
        """Init Method """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area Method"""

        return self.__size ** 2
