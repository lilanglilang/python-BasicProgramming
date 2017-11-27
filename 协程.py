#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
协程，又称微线程，纤程。英文名Coroutine。
子程序调用是通过栈实现的，一个线程就是执行一个子程序
子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多
'''
def consumer():
    r = ''
    while True:
        n =yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
