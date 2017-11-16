#！user/bin/env python3
# -*- coding:utf-8 -*-
class Goole():
    def __init__(self):
        self.code=""
        pass
Goole.tom="伟大的工程师"
print(Goole.tom)
# Goole().name="对象赋值"
# print(Goole().name) 错误的写法
name=Goole()
name.tome="你好"
name.absmy=abs
print(name.tome)
print(name.absmy(5))
def myfunction(a):
    print(a)
Goole.absown=myfunction
Goole.absown("python 你好")
#为了给所有实例都绑定方法，可以给class绑定方法：
# 给一个实例绑定的方法，对另一个实例是不起作用的
# 除非在子类中也定义__slots__，这样，
# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class myfunc(object):
    __slots__ = ('sex','name')#对实例化后的对象起作用
    pass
myfunc.baidu='你好，世界'
print(myfunc.baidu)
##你好，世界
myfunc=myfunc()
myfunc.haha="你好"
'''
myfunc.haha="你好"
AttributeError: 'myfunc' object has no attribute 'haha'
'''


