#!/usr/bin/python3
"""Square Class."""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): Teh size of the squre.
    """

    def __init__(self, size) -> None:
        """
        Initialize a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
