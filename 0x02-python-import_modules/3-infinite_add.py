#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    res = 0
    for x in range(1, n):
        res += int(sys.argv[x])
    print('{}'.format(res))
