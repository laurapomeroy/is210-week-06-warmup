#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping lists"""


def process_data(data):
    """Returns a tuple containing the data point in-order

    Args:
        data (mixed): List of tuple numbers

    Returns:
        tuple: Lists the sums and averages

    Examples:

    >>> process_data([1, 2, 3])
    (6, 2.0)

    """

    mysum = 0
    for item in data:
        mysum += item
    myavg = mysum / float(len(data))
    
    return (mysum, myavg)
