#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class person(object):
    def _hello(self):
        print("huanren")
'''
单前置下划线表示保护属性或者方法 from somemodel import * 禁止导入
类对象和子类可以访问
后置单下划线区分变量名
'''
lilang=person()
lilang._hello() #可以访问
class Man(person):
    def __init__(self):
        super(Man).__init__()
lang=Man()
lang._hello()
