#!/use/bin/python3
"""
magic_string module.

This module defines a function to generate a magical string\
    containing the phrase "BestSchool".
"""


def magic_string() -> str:
    """Generate a magical string."""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool, " * (magic_string.n - 1) + "BestSchool"
