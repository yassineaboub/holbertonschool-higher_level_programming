#!/usr/bin/python3
for i in range(10):
    for n in range(10):
        if i == 8 and n == 9:
            print("89")
        elif i < n:
            print("{0:d}{1:d}, ".format(i, n), end="")
