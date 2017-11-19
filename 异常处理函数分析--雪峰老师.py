#！user/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce
import  re
def str2num(s):
  return int(re.sub("\D","",s))#去除非数字字符
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    blc = calc('99 +7.6 +88')
    print('99 + 88 + 7.6 =', blc)
main()
