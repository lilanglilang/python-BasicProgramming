#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
a=[1,2,3,4]
print(isinstance(a,Iterable))#判断是否是迭代对象，生成器一定是迭代器
string='1000'
b=iter(string)#有些课迭代的东西不一定是迭代对象，把可迭代对象转化为迭代对象，占用的内存空间一定要小
for i in b:
    print(i)
