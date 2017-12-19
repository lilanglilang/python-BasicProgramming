#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))
print(sum([1,3,5,7,9]))

def funcAdd(x,y):
    return x*10+y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def checkname(s):
    return s.lower()
he=map(checkname,["AFASF","AFASF","AFASF","AFASF","ASDFSDAFSAD"])
print(list(he))
def helo(s):
    print(s)
data=(x for x in range(1,10))#生成迭代器对象