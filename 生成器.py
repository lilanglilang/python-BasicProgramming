#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def _old_iter():
    n=1
    while True:
        n=n+2
        yield n
def not_divisibale(n):
    return  lambda x:x%n>0
def generater():
    yield 2
    it=_old_iter()
    while True:
        n=next(it)
        yield n
        it=filter(not_divisibale(n),it)
for n in  generater():
    if n<10:
        print(n)
    else:
        break