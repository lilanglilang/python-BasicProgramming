#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def lay_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lay_sum(1,2,3,4,5,6)
print(f())
#输出结果 21
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且
#内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1=lay_sum(1,2,3,4,5,6)
print(f==f1)
#输出结果false
def count():
    fs = []
    for i in range(1, 4):
        def function():
             return i*i
        fs.append(function)
    return fs
myf=[]
myf=count()
#[<function count.<locals>.function at 0x000001F984ABC8C8>, <function count.<locals>.function at 0x000001F984ABCA60>, <function count.<locals>.function at 0x000001F984ABCAE8>]
for x in  myf:
    print(x())
#9,9,9 不是1,4,9原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
a,b,c=[1,2,3]
print(a) #1
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
'''
小结

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
'''