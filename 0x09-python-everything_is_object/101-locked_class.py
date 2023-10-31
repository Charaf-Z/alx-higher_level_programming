#!/usr/bin/python3
"""Defines a locked class with restricted attribute creation."""


class lockedClass:
    """
    A class that allows the creation of only one instance attribute,\
    ``first_name``.

    Attributes:
        __slots__ (list): A list containing only ``first_name`` to restrict\
            attribute creation.
    """

    __slots__ = ["firt_name"]
