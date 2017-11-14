#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
f=lambda x:x*x
print(f)
print(f(5))
def function(x,y):
    return lambda : x*y
#也可以把匿名函数作为返回值返回，
f=function(5,6)
print(f())