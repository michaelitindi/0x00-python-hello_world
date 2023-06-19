#!/usr/bin/python3
"""Class Base """


class Base:
    """ The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json for list dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string rep """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        jstring = cls.to_json_string([obj.to_dictionary()for obj in list_objs])
        with open(filename, "w") as file:
            file.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with all attributes"""
        if cls.__name__ == "Rectangle":
            dm = cls(1, 1)
        elif cls.__name__ == "Square":
            dm = cls(1)
        else:
            dm = None

        dm.update(**dictionary)
        return dm

    @classmethod
    def load_from_file(cls):
        """ returns list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                j_string = file.read()
                dicts = cls.from_json_string(j_string)
                instances = [cls.create(**dictionary) for dictionary in dicts]
                return instances
        except FileNotFoundError:
            return []
