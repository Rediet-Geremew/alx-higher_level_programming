#!/usr/bin/python3
def islower(c):
    order = ord(c)

    if order > 96 and order < 123:
        return True
    else:
        return False
