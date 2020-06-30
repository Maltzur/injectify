"""This module contains the data structures that power Injectify."""

from typing import Sequence


class listify(list):
    """Convert an object into a list.

    A ``list``-like object that wraps an object into a list if it is not
    a sequence, or converts the object to a list if it is a sequence.
    """

    def __init__(self, initlist):
        if initlist is not None:
            if isinstance(initlist, list):
                self[:] = initlist
            elif isinstance(initlist, Sequence):
                self[:] = list(initlist)
            else:
                self.append(initlist)
