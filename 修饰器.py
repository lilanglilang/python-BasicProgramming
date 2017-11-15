#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#装饰器:我们重新定义修饰函数，称为装饰器，本质上就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print("2017-11-14")
now()
# call now():
# 2017-11-14
#装饰器原来的now()函数仍然存在，只是现在同名的now变量指向了新的函
#数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，
#首先打印日志，再紧接着调用原始函数。
'''
输出结果
call now():
2017-11-14
'''
def funcrtion(*args,**ks):
    print(args,ks)
funcrtion((1,2,3,5),(2,3,4,5,5,6),[1,2,3,4,5,6,6,7],city="北京",world='你好')
#((1, 2, 3, 5), (2, 3, 4, 5, 5, 6), [1, 2, 3, 4, 5, 6, 6, 7]) {'city': '北京', 'world': '你好'}这样更好理解，可以接收任何参数
funcrtion()#() {}
#带有参数的修饰器


import  time
def timeSpend(func):
    def wap(a,b):
        startTime=time.time()
        func(a,b)
        endTime=time.time()
        sumTime=(endTime-startTime)*1000
        print("花费时间是:%s"%sumTime)
    return wap

@timeSpend
def gogogo(a,b):
    print("裝飾器你好：")
gogogo(1,3)
'''
裝飾器你好：
花费时间是:0.0
'''
@log
@timeSpend
def gogogo(a,b):
    print("裝飾器你好：")
gogogo(1,3)
'''
如果装饰器需要传入参数
'''
def mylog(func):
    def wapper(*args,**kws):
        print('%s %s %s():' % (args,kws, func.__name__))
        return func(*args, **kws)
    return wapper
def hello(func):
    def warpper(*args,**kws):
        print("#################################")
    return warpper
@mylog
def whatName(a,b):
    print("你好，汪峰")
whatName(1,2)# def wapper(*ars,**kws):接收的参数是函数传进去的变量
import  functools
def log(text):
    '''一个装饰器函数'''
    def derector(func):
        @functools.wraps(func)#wrapper.__name__ = func.__name__
        #wrapper在实现前加入 @functools.wraps(func) 可以保证装饰器不会对被装饰函数造成影响 目前还不是很明白
        def wrapper(*args,**kws):
            print("%s %s():"%(text,func.__name__))
            print(*args)
            return func(*args,**kws)
        return  wrapper
    return derector
@log("excute")
def now(a,b):
    print("2017-11-15")
now(1,2)
'''
excute now():
1 2
2017-11-15
'''
print(now.__name__)
