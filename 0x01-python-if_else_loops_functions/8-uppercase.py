#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= ord('a') and c <= ord('z'):
            c -= 32
        print("{:c}".format(c), end="")
    print("")
