#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            i = ord(char)
            i = i - 32
            char = chr(i)
        print("{}".format(char), end="")
    print("")
