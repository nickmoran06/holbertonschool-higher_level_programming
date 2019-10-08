#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        # return height
        return self.__height

    @height.setter
    # receive the height value
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        # return width
        return self.__width

    @width.setter
    # receive the width value
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
