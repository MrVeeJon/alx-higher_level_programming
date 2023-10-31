#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything except for attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
