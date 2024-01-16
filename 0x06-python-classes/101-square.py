#!/usr/bin/python3
'''Contains square class'''


class Square:
    """ Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Init Method """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Size setter"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position Getter """
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter """
        if type(value) != tuple or len(value) != 2 \
                or type(value[0]) != int or \
                type(value[1]) != int or value[0] < 0 \
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area Method"""

        return self.__size ** 2

    def my_print(self):
        ''' Prints the square '''

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    def __str__(self):
        """ Prints a square instance """

        rep = ''
        if self.__size == 0:
            return ''
        else:
            for i in range(self.__position[1]):
                rep += '\n'
            for j in range(self.__size):
                rep += ' ' * self.__position[0]
                rep += '#' * self.__size + '\n'
            return rep[:-1]
