#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx >= len(my_list)):
        return my_list
    else:
        del mylist[idx]
        return mylist
