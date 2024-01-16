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

    def my_print(self):
        ''' Prints the square '''

        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()

        if self.__size == 0:
            print()
