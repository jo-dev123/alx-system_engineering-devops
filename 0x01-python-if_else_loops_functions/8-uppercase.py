#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        store = ord(str[i]) - 32
        print("{:s}".format(store), end='')
