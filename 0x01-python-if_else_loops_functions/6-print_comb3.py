#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if ((j != i) and (j > i)):
            if (i == 8 and j == 9):
                print("89")
            else:
                print("{:d}{:d}".format(i, j), end=", ")
