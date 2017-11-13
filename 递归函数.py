#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fact(n,):
    if n<=0:
      return 0;
    elif n==1:
        return 1
    return fact(n,1)
n=fact(5)
print(n)