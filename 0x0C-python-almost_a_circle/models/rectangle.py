#!/usr/bin/python3
"""
Module of the rectangle class
"""
from models import base
Base = base.Base


class Rectangle(Base):
    """
    Rectangle representation
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the atributtes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the width"""
        return self.__width

    @property
    def height(self):
        """Return the height"""
        return self.__height

    @property
    def x(self):
        """Return the value of x"""
        return self.__x

    @property
    def y(self):
        """Return the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle"""
        rectangle = ("\n" * self.__y)
        for height in range(self.__height):
            rectangle += (" " * self.__x)
            rectangle += ("#" * self.__width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """String representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Method to update the values of the rectangle"""
        list_of_values = ["id", "width", "height", "x", "y"]

        for i, value in enumerate(args):
            setattr(self, list_of_values[i], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of the rectangle"""
        return {"x": self.x, "y": self.y, "height": self.height,
                "width": self.width, "id": self.id}
