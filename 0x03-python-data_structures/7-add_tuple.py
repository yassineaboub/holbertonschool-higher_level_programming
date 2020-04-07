#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = list(tuple_a)
    if len(tup_a) < 2:
        for x in range(len(tup_a), 2):
            tup_a.append(0)
    tup_b = list(tuple_b)
    if len(tup_b) < 2:
        for x in range(len(tup_b), 2):
            tup_b.append(0)

    tup_ab = (tup_a[0] + tup_b[0], tup_a[1] + tup_b[1])
    return(tup_ab)
