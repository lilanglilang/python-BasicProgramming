#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
== is
判断内容用等号
判断是否是指向相同的时候用is
'''
import copy
#（3）深拷贝，包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
#如果拷贝的对象是不可变类型，则直接执行浅拷贝
print("###############")
dep=[12,232,344,[12,222,33,55]]
depc=copy.deepcopy(dep)
print(depc)
print(dep)
dep[3].append("fsadfsfdsfds")
print(dep)
print(depc)
'''
[12, 232, 344, [12, 222, 33, 55]]
[12, 232, 344, [12, 222, 33, 55]]
[12, 232, 344, [12, 222, 33, 55, 'fsadfsfdsfds']]
[12, 232, 344, [12, 222, 33, 55]]
'''
print("###############")
ep=[12,232,344,[12,222,33,55]]
pc=copy.copy(ep)
print(pc)
print(pc)
ep[3].append("fsadfsfdsfds")
print(pc)
print(pc)
'''
浅拷贝
[12, 232, 344, [12, 222, 33, 55]]
[12, 232, 344, [12, 222, 33, 55]]
[12, 232, 344, [12, 222, 33, 55, 'fsadfsfdsfds']]
[12, 232, 344, [12, 222, 33, 55, 'fsadfsfdsfds']]
'''

print("###############")
ep=[12,232,344,[12,222,33,55]]
pc=ep
print(pc)
print(pc)
ep[3].append("fsadfsfdsfds")
print(pc)
print(pc)
'''
浅拷贝
[12, 232, 344, [12, 222, 33, 55]]
[12, 232, 344, [12, 222, 33, 55]]
[12, 232, 344, [12, 222, 33, 55, 'fsadfsfdsfds']]
[12, 232, 344, [12, 222, 33, 55, 'fsadfsfdsfds']]
'''
tup=(1,2,3,4,5)
print(tup)
print(tup[1])
