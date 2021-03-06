#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    p1 = 0
    p2 = 0
    for (s, w) in my_list:
        p1 += s * w
        p2 += w
    return p1/p2
