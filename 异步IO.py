#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
import  asyncio
@asyncio.coroutine
def huanren():
    print("huanren world")
    r=yield from asyncio.sleep(1)
    print('huanren again')
loop=asyncio.get_event_loop()
loop.run_until_complete(huanren())
loop.close()
'''

'''
@asyncio.coroutine把一个generator标记为coroutine类型，
然后，我们就把这个coroutine扔到EventLoop中执行。
huanren()会首先打印出Hello world!，然后，
yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，
而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，
线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句
最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，
也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，
所以执行效率比多线程高很多
n=0
import asyncio
import threading
@asyncio.coroutine
def huanren():
    global n
    n=n+1
    print(n)
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())
task=[]
for i in  range(1000):
    task.append(huanren())
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
loop.close()
'''

'''
由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
'''
import asyncio
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect=asyncio.open_connection(host=host,port=80)
    reader, writer = yield from connect
    header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
asyncio提供了完善的异步IO支持；

异步操作需要在coroutine中通过yield from完成；

多个coroutine可以封装成一组Task然后并发执行
'''