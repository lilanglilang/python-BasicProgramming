#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
#int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
def int2(x):
    return int(x,base=2)
print(int2('1000')) #8
import  functools
int8=functools.partial(int,base=8)
int8('12337')