#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
python的线程是真正的线程，并不是模拟出来的
Python的标准库提供了两个模块：
_thread和threading，_thread是低级模块，
threading是高级模块，对_thread进行了封装
'''
'''
import  time,threading
def loop():
    print("thread %s is running..."%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print("thread %s >>>%s"%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'%threading.current_thread().name)
print("thread %s is running ..."%threading.current_thread().name)
t=threading.Thread(target=loop,name='loopthread')
t.start()
t.join()
print('thread %s ended '%(threading.current_thread().name))
'''
#多进程中，同一个变量，各自有一备份拷贝在自己的内存中，互相不影响
#多线程中，所有的变量让线程共享
'''
import time,threading
balance=0;
def chang_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(t):
    for i in range(1000000):
        chang_it(t)
t1=threading.Thread(target=run_thread,name='thread lee',args=(5,))
t2=threading.Thread(target=run_thread,name='thread lang',args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)#23,5等等
'''
'''
import time,threading
balance=0;
def chang_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread():
    for i in range(1000000):
        chang_it(i)
t1=threading.Thread(target=run_thread,name='thread lee')
t2=threading.Thread(target=run_thread,name='thread lang')
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)#17070,1346532等等
'''
# 线程上锁
'''
import time,threading
balance=0;
block=threading.Lock()
def chang_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread():
    for i in range(1000000):
        block.acquire()
        try:
            chang_it(i)
        finally:
            block.release()
t1=threading.Thread(target=run_thread,name='thread lee')
t2=threading.Thread(target=run_thread,name='thread lang')
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
import time,threading
balance=0;
block=threading.Lock()
def chang_it(n):
    global balance
    block.acquire()
    try:
        balance=balance+n
        balance=balance-n
    finally:
        block.release()
def run_thread():
    for i in range(10000000):
       chang_it(i)
t1=threading.Thread(target=run_thread,name='thread lee')
t2=threading.Thread(target=run_thread,name='thread lang')
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

import time,threading
balance=0;
block=threading.Lock()
def chang_it(n):
    block.acquire()
    # 只要操作共享变量的地方锁住就ok了
    try:
        global balance
        balance=balance+n
        balance=balance-n
    finally:
        block.release()
def run_thread():
    for i in range(10000000):
       chang_it(i)
t1=threading.Thread(target=run_thread,name='thread lee')
t2=threading.Thread(target=run_thread,name='thread lang')
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦
在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，
解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
'''