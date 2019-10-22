#!/usr/bin/python3

from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initilize the values of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Returns the size value"""
        return super().width

    @size.setter
    def size(self, value):
        """Setter for the square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update the values of the square"""
        list_of_values = ["id", "size", "x", "y"]

        for i, value in enumerate(args):
            setattr(self, list_of_values[i], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of the square"""
        return {"x": self.x, "y": self.y, "size": self.size, "id": self.id}
