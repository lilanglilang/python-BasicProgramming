#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import os,time,random
def write(q):
    print("Process to write:%s"%os.getpid())
    for vaule in ['a','b','c']:
        print('put %s to queue!'%vaule)
        q.put(vaule)
        time.sleep(random.random())
def read(q):
    print("Process to read:%s"%os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue.'%value)
if __name__=='__main__':
    q=Queue()
    #启动子进程，并且传递给各个子进程
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动子进程
    pr.start()
    pw.start()
    #等待pw结束
    pw.join()
    #强行结束
    pr.terminate()
'''
Process to read:5596
Process to write:6040
put a to queue!
Get a from queue.
put b to queue!
Get b from queue.
put c to queue!
Get c from queue.
'''
