#!/usr/bin/python3
"""Class to JSON
"""


def Class_to_json(obj):
    """Return the dictionary represaentation
    of a simple data structure.

    """
    return obj.__dict__
