#！user/bin/env python3
# -*- coding:utf-8 -*-
def foo(s):
   n=int(s)
   assert n!=0,'n is zero!'
   return 10/n
def main():
    foo(1)
main()
'''
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

$ python -O err.py
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
'''
#logging
import logging
logging.basicConfig(level=logging.INFO,filename='hello.txt')
s='0'
n=int(s)
logging.info("n=%d"%n)
logging.error("fasdfsd")
print(n/1)
def baidu():
    print("baidu")
if __name__=='__main__':
    baidu()
