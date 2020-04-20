#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicc = dict(a_dictionary)
    for i in dicc:
        dicc[i] *= 2
    return (dicc)
