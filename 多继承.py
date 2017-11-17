#！user/bin/env python3
# -*- coding:utf-8 -*-
'''
MixIn在设计类的继承关系时，通常，主线都是单一继承下来
但是如果需要“混入”额外的功能，通过多重继承就可以实现
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候
我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须
使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。
通过组合，我们就可以创造出合适的服务来。
'''
from socketserver import ForkingMixIn, TCPServer, ThreadingMixIn, UDPServer

#自定义出来的tcp服务，一个多进程模式的TCP服务
class MyTcpServer(TCPServer,ForkingMixIn):
    pass
#编写一个多线程模式的UDP服务
class MyUDPServer(UDPServer,ThreadingMixIn):
    pass
#搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# 只允许单一继承的语言（如Java）不能使用MixIn的设计,但是java提供了接口设计