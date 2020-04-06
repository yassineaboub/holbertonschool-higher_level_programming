#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    if idx < 0:
        return (newlist)
    if idx > len(my_list):
        return (newlist)
    else:
        newlist[idx] = element
        return (newlist)
