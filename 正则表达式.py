#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#用\d可以匹配一个数字，\w可以匹配一个字母或数字
'''
用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
\d{3}表示匹配3个数字，例如'010'
\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
\d{3,8}表示3-8个数字，例如'1234567'。
\d{3}\s+\d{3,8}。正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，
在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}
要做更精确地匹配，可以用[]表示范围，比如：

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，
后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。
但是加上^py$就变成了整行匹配，就只能匹配'py'了。
'''

#re模块
import re
s='abc\\-001'
# 对应的正则表达式字符串变成：
# 'ABC\-001'
#强烈使用r 不考虑转义问题
strl=r'abc\-012'
if re.match(r'\d{3}\-\d{3,8}$','123-213'):
    print("yes it matched")
'''
match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
'''
#切分字符串
print('ab c'.split(' ')[0])
print(re.split(r'\s+','sdffsad   '))
#分组用()表示的就是要提取的分组（Group）。比如：
m=re.fullmatch(r'(^(\d{3})-(\d{3,8}))','012-343')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
##注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
print(re.match(r'^(\d+)(0*)$','121221212132312320000').groups())
'''
>>> re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')
由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
'''
print(re.match(r'^(\d+?)(0*)$','121221212132312320000').groups())
'''
如果一个正则表达式要重复使用几千次，出于效率的考虑，
我们可以预编译该正则表达式，
接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
telepahone=re.compile(r'(\d{3})-(\d{3,8})$')
print(telepahone.match('123-4567788').groups())
#email
email_match=re.compile(r'([a-zA-Z1-9]+?)@(qq|gmail|163).(\w+)')
print(email_match.match("someon1212e@gmail.com").groups())
print(email_match.match("soaSFDF@163.com").groups())