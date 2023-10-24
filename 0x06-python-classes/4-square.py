#!/usr/bin/python3
"""Access with setter private attribute"""


class Square:
    """Private instance attribute size, property and setter"""

    def __init__(self, size=0):
        """creation of attribute size """
        self.__size = size

    def area(self):
        """Sqre area calc"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

