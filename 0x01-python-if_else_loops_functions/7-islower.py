#!/usr/bin/python3
def islower(c):
    ascii_v = ord(c)
    if (ascii_v >= ord("a") && ascii_v <= ord("z")):
        return True
    else:
        return False
