#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，
一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
而子进程只需要调用getppid()就可以拿到父进程的ID。
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid=os.fork()
if pid==0:
    print("I am child process (%s) and my parent is %s"%(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
from multiprocessing import Process
import os
# #子进程要执行的代码
# def run_proc(name):
#     print("Run child process %s (%s)..."%(name, os.getpid()))
# if __name__=='__main__':
#     print("Parent process %s."%os.getpid())
#     '''
#     >>> t = (1)
#     >>> t
#     1
#     定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
#     又可以表示数学公式中的小括号，这就产生了歧义，
#     因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#     '''
#     p=Process(target=run_proc,args=('test',))
#     print("child process will start")
#     p.start()
#     p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     print("child process end")

from multiprocessing import Pool
import time,random
def long_time_task(name):
    print("run task %s  (%s)..."%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print("task %s run %0.2f seconds."%(name,(end-start)))
if __name__=='__main__':
    print("parent process %s"%os.getpid())
    p=Pool(4)
    '''
    请注意输出的结果，task 0，1，2，3是立刻执行的，
    而task 4要等待前面某个task完成后才执行，
    Pool的默认大小在我的电脑上是4，
    因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
    '''
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done..')
    for i in  range(5):
        print(i)#0,1,2,3,4
    import subprocess

    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
    print("你好")
