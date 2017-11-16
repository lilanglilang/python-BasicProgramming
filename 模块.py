#! /user/bin/env python3
# -*- coding: utf-8 -*-
'''
作用域

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，
__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
'''
def _private_function():
    name="lilang"
    _city="jinan"
    print("hello")
from PIL import Image as image
im=image.open('E:\\timg.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('E:\\thumb', 'PNG')
