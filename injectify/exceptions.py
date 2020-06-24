"""This module contains exceptions that power Injectify."""


class ClassFoundException(Exception):
    """Exception for when a class cannot be found.

    Raised when a class cannot be found when getting the source code.
    """
