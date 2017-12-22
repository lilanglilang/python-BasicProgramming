#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
a=[1,2,3,4,5,6,6]
b=[2,3,4,5,6,7,8]
print(a[::2])
print(a[::-2])
print(dict(zip(a,b)))
print(sorted(a,reverse=True))
random.shuffle(a)
print(a)
