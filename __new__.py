#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class ChuShiHua(object):
    def __init__(self):
        print("__init__执行")
    def __del__(self):
        print("ChuShiHua对象销毁")
    def __new__(cls, *args, **kwargs):
        print("__new__方法执行了")
        return super(ChuShiHua,cls).__new__(cls)
    #或者 super().__new__(cls)
hello=ChuShiHua()