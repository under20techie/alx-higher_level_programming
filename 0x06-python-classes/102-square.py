#!/usr/bin/python3
"""Contains sqaure class """


class Square:
    """ Square class"""
    def __init__(self, size=0):
        """Init Method """

        self.size = size

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Size Getter"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area Method"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal """ 
        return self.__size == other

    def __ne__(self, other):
        """ Not Equal """
        return self.__size != other

    def __ge__(self, other):
        """Greater than or equal to """
        return self.__size >= other

    def __gt__(self, other):
        """Greater than """
        return self.__size > other

    def __le__(self, other):
        """Less than or equal to """
        return self.__size <= other

    def __lt__(self, other):
        """Less than or equal to """
        return self.__size < other
