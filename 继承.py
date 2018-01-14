#!/usr/bin/env python3
# -*- coding: utf-8 -*
class A(object):
    num=0
    def __init__(self):
        #实例属性
        self.name='helo'
        self.__age='23'
        self._sex='男'
    def printHello(self):
        print("hello")
class B(A):
    def haha(self):
        super().printHello()
b=B()
print(b.name)
print(b._sex)
print(b.num)
# print(b.__age) 私有属性不允许使用
'''
helo
男
object has no attribute '__age'
'''
# class C(A,B):
#   pass
# print(C.__mro__)
# '''
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
# '''
class C(B,A):
  pass
print(C.__mro__)
'''
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
'''