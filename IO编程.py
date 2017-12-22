#！user/bin/env python3
# -*- coding:utf-8 -*-
'''
读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
或者把数据写入这个文件对象（写文件）。
读文件
要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，
并且操作系统同一时间能打开的文件数量也是有限的：
但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便：
'''
import logging
logging.basicConfig(filename='huanren.txt')
try:
    file = open("huanren.txt", 'r',encoding='utf-8')
    print(file)
    data = file.read()
    print(data)
except IOError:
    pass
finally:
    file.close()
with open("huanren.txt", 'r',encoding='utf-8') as  f:
    print(f.read())
file = open("huanren.txt", 'r',encoding='utf-8')
for line in file.readlines():
    print(line+"你好")
file.close()
'''
二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
'''
f=open('yaya.jpeg','rb')
print(f.read())
f.close()
'''
字符编码
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
因为在文本文件中可能夹杂了一些非法编码的字符。
遇到这种情况，open()函数还接收一个errors参数，
表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
'''
file=open('huanren.txt','r',encoding='utf-8',errors='ignore')
print(file.read())
'''
写文件和读文件是一样的，唯一区别是调用open()函数时，
传入标识符'w'或者'wb'表示写文本文件或写二进制文件
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
空闲的时候再慢慢写入。只有调用close()方法时，
操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，
剩下的丢失了。所以，还是用with语句来得保险：

with open('huanren.txt','w') as f:
    f.write("你是猪么")
    #������出现了乱码
with open('huanren.txt','w',encoding='utf-8') as f:
    f.write("你是猪么")
'''
fpath=r'E:\查询指定微博数据.txt'
with open(fpath,'r',encoding='utf-8') as excel:
    s=excel.read()
    print()

