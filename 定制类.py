#！user/bin/env python3
# -*- coding:utf-8 -*-
#注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
class MyOwnClass(object):
    #__slots__ = ('__name')#实例化类只能接受name参数
    def __init__(self):
        self.google='Google是个伟大的公司'
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    def __str__(self):
        return self.name
    def __getattr__(self,attr):
        if attr=="python":
            print("你是一个聪明的人，加油！")
    def __call__(self, *args, **kwargs):
        '''
        个对象实例可以有自己的属性和方法，当我们调用实例方法时，
        我们用instance.method()来调用。能不能直接在实例本身上调用呢
        :param args:
        :param kwargs:
        :return:
        '''
        print("你好，世界！")
        return "python"
own=MyOwnClass()
own.name='langlang'
name=own.name
print(name)
varn=MyOwnClass()
varn.python
callname=MyOwnClass()
print(callname())
print(callable(callname))#判断对象能否被调用
