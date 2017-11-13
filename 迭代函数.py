#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from collections import Iterable
# dict={'name':'lilang','address':'北京市','phone':'18253291926'}
# for n in dict:
#     print(n)
# for n in dict.values():
#     print(n)
# for key,value in  dict.items():
#     print(key,value)
# str="baidu"
# for n in  str:
#     print(n)
# if isinstance(str,Iterable):
#     print("yes")
# list=['baidu','nihao','tenxun']
# for i,value in enumerate(list):
#     print(i,value)
print(list(range(1,10)))
print(tuple(range(1,10)))
dic={'name':'beijing'}
print({n:v for n,v in dic.items()})
list=[m+n for m in  'ABC' for n in 'abc']
print(list)

import  os
listdir=[d for d in os.listdir()]
print(listdir)

L=['BAIDU']
list=[s.lower() for s in L]
print(list)


L = ['Hello', 'World', 18, 'Apple', None]
list=[n.lower()  for n in  L if isinstance(n,str)]
print( list)
print(isinstance("我",str))