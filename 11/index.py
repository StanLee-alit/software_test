#!/usr/bin/env python
from turtle import right


def coverage(x, y):
    gift = 0
    if x > 0 and y > 0:
        gift = x+y+5
        print("语句块1")
    else:
        gift = x+y-5
        print("语句块2")
    if gift < 0:
        gift = 0
        print("语句块3")
    print("语句块4")
    return gift


result = coverage(1, 2)
print(result)
