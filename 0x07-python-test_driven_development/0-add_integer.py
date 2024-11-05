#!/usr/bin/python3
"""
Module for add_integer function.
This module provides a function to add two integers or floats,
converting them to integers if necessary.
"""


def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
