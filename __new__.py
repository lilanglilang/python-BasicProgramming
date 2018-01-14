#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class ChuShiHua(object):
    def __init__(self):
        print("__init__执行")

    def __del__(self):
        print("ChuShiHua对象销毁")

    def __new__(cls, *args, **kwargs):
        print("__new__方法执行了")
        return super(ChuShiHua, cls).__new__(cls)
        # 或者 super().__new__(cls)


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, status_number):
        self.status_number = status_number


h = Singleton("fs")
h2 = Singleton("fds")
print(h2.status_number)


class oneInstance():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)  # python3直接这样写就行
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        self.name = name


one = oneInstance("你好")
twohehe = oneInstance("hello")
print(id(one))
print(id(twohehe))

