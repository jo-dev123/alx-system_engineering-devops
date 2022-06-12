#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        anotherstr = str[:n] + str[n + 1:]
        return (anotherstr)
    else:
        return (str)
