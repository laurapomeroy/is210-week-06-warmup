#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability differences between strings and their cousin, the tuple"""


def flip_keys(to_flip):
    """List and reverse the order of the inner sequence.

    Args:
        to_flip(list): A nested list with immutable sequences.

    Returns:
        The original list with the items reverse

    Example:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'abc']

    """
    numbers = 0
    for item in to_flip:
        to_flip[numbers] = item[::-1]
        numbers += 1
    
    return to_flip
