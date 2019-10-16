#!/usr/bin/python3
class MyList(list):
    """A class that inherits from a parent class list"""

    def __init__(self):
        """Initializes from the parent class"""
        super().__init__()

    def print_sorted(self):
        """Print the list in ascending sort"""
        print(sorted(self))
