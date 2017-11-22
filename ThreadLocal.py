#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
local_stu=threading.local()
def process_student():
    stu=local_stu.student
    print("hello %s (in %s)"%(stu,threading.current_thread().name))
def process_thread(name):
    local_stu.student=name
    process_student()
t1=threading.Thread(target=process_thread,args=('bob',),name='thrad_bob')
t2=threading.Thread(target=process_thread,args=('alice',),name='thread_alice')
t1.start()
t2.start()
t1.join()
t2.join()
'''
全局变量local_school就是一个ThreadLocal对象，
每个Thread对它都可以读写student属性，但互不影响。
你可以把local_school看成全局变量，
但每个属性如local_school.student都是线程的局部变量，
可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，
互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
多线程模式通常比多进程快一点，但是也快不到哪去，
而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，
因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，
你经常可以看到这样的提示：
该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
'''