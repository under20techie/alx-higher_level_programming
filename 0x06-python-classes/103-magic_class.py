#!/usr/bin/python3
"""Contains square class """
import math


class MagicClass:
    """ Magic Class"""

    def __init__(self, radius=0):
        """ Init Method"""
        self.radius = radius

    @property
    def radius(self):
        """ Getter """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """ Setter """
        if type(value) is not int:
            if type(value) is not float:
                raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Area Method"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Circumference """
        return 2 * math.pi * self.__radius
