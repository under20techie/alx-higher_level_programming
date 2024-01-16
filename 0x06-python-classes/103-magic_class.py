#!/usr/bin/python3
"""Contains square class """
import math


class MagicClass:
    """ Magic Class"""

    def __init__(self, radius):
        """ Init Method"""
        self.radius = radius

    @property
    def radius(self):
        """ Getter """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """ Setter """
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Area Method"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Circumference """
        return math.pi * self.__radius
