#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        store = my_list[0]
        for i in my_list:
            if i > store:
                store = i
        return store
    return None
