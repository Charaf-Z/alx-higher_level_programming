#!/usr/bin/python3
"""Module with a Base class and utility functions for working with shapes."""

from json import dumps, loads
from csv import DictWriter, DictReader
import turtle


class Base:
    """Base class for managing shapes."""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialize a Base instance.

        Args:
            id (int, optional): The identifier for the instance.
                If None, a unique identifier will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON-formatted string.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs) -> int:
        """Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to save.

        Returns:
            int: The number of characters written to the file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as fp:
            if list_objs is None:
                fp.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                fp.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string) -> list:
        """Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): JSON-formatted string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary) -> 'Base':
        """Create a new instance based on a dictionary.

        Args:
            dictionary (dict): Dictionary containing object attributes.

        Returns:
            Base: New instance created from the dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            return new_instance.update(**dictionary)

    @classmethod
    def load_from_file(cls) -> list:
        """Load a list of objects from a JSON file.

        Returns:
            list: List of loaded objects.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as fp:
                list_dicts = Base.from_json_string(fp.read())
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs) -> None:
        """Save a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to save.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as fp:
            if list_objs is None or list_objs == []:
                fp.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                toWrite = DictWriter(fp, fieldnames=fieldname)
                for obj in list_objs:
                    toWrite.writerow(obj.to_dictionary())

    @classmethod
    def load_from_csv(cls) -> list:
        """Load a list of objects from a CSV file.

        Returns:
            list: List of loaded objects.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as fp:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                list_dicts = DictReader(fp, fieldnames=fieldname)
                list_dicts = [
                    dict([key, int(value)] for key, value in d.items())
                    for d in list_dicts
                ]
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares) -> None:
        """Draw rectangles and squares using the turtle graphics library.

        Args:
            list_rectangles (list): List of rectangles to draw.
            list_squares (list): List of squares to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#a6a6a6")
        turt.pensize(2)
        turt.shape("turtale")

        turt.color("#af0000")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#0d47cc")
        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sqr.y)
            turt.down()
            for _ in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()