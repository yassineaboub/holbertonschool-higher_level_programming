#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = abs(number) % 10
if number < 0:
    l = -l
print("Last digit of {} is {} and is ".format(number, l), end="")
if l > 5:
    print("greater than 5")
elif l == 0:
    print("0")
else:
    print("less than 6 and not 0")
