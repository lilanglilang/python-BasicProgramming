#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Demo(object):
    def __init__(self):
        self.__num=''#对于一个对象（变量）来说，引用次数必须是大于0的，否则会被虚拟机回收
    def setNum(self,newNum):
        self.__num=newNum
    def getNum(self):
        return self.__num
    num=property(getNum,setNum)
t=Demo()
t.num=10000
print(t.num)
class Demo2(object):
    def __init__(self):
        self.__money=''

    @property
    def Money(self):
        '''相当于返回一个变量值'''
        return self.__money
    @Money.setter
    def Money(self,newMoney):
        self.__money=newMoney
k=Demo2()
k.Money=100
print(k.Money)


