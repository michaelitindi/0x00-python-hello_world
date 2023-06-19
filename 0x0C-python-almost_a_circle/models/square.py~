#!/usr/bin/python3
""" square class that inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ init of square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            att = ["id", "size", "x", "y"]
            for i, arg in enumerate(args[:len(att)]):
                setattr(self, att[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ str rep"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
