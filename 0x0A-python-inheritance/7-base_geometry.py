#!/usr/bin/python3
"""BaseGeometry Class."""


class BaseGeometry:
    """Base geometry class representation."""

    def area(self) -> int:
        """Calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value) -> None:
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
