#!user/bin/env python3
# -*- coding:utf-8 -*-
import os
print(os.name)#nt windows系统 如果是posix，说明系统是Linux、Unix或Mac OS X、
#获取详细的系统信息os.uname注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
print(os.environ)#获取环境变量
print(os.path.abspath("."))#获取当前目录的绝对路径
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符
# os.mkdir(os.path.join(os.path.abspath("."),"python"))
# os.rmdir(os.path.join(os.path.abspath("."),"python\lilang.txt"))
'''
拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
'''
print(os.path.splitext('/path/to/file.txt'))
print(os.path.split('/path/to/file.txt'))
'''
('/path/to/file', '.txt')
('/path/to', 'file.txt')
os.rename("hello.py",'hello.txt')
os.remove("")#删掉文件
'''

'''
幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
'''
import  shutil
list_file=[x for x in os.listdir(".")]#['.git', 'hello.txt', 'IO编程.py', 'map_reduce.py', 'property.py', 'python', 'README.md', 'timg.jpg', 'yaya.jpeg', '修饰器.py', '偏函数.py', '内存读写.py', '函数作为返回函数.py', '切片问题.py', '匿名函数.py', '多继承.py', '定制类.py', '异常处理函数分析--雪峰老师.py', '文件和目录.py', '枚举类.py', '模块.py', '生成器.py', '类.py', '访问限制.py', '调试.py', '迭代函数.py', '递归函数.py', '错误处理.py', '面向对象高级编程.py']
print(list_file)
list_py=[x for  x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']#过滤当前目录下所有的py文件
print(list_py)
for x in os.listdir("."):
    if(os.path.isfile(x)):
        print(os.path.split(x))
        '''
        ('', '切片问题.py')
        ('', '匿名函数.py')
        ('', '多继承.py')
       '''
from datetime import datetime
import os
pwd = os.path.abspath('.')
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')
for f in os.listdir(pwd):
    if not os.path.splitext(f)[1]=='.py':
        continue
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M:%S')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))