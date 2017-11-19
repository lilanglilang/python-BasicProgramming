# ！user/bin/env python3
# -*- coding:utf-8 -*-
'''
StringIO
很多时候，数据读写不一定是文件，也可以在内存中读写。
StringIO顾名思义就是在内存中读写str。
'''
from io import StringIO
f=StringIO()
flag=f.write("hello")
flag=f.write("helloli")
flag=f.write("hellowo")
print(flag)#5
print(f.getvalue())
f=StringIO("hello\nHi\npython\n")
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
'''
BytesIO

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
请注意，写入的不是str，而是经过UTF-8编码的bytes。

和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
'''
from io import BytesIO
f=BytesIO()
f.write("百度".encode("utf-8"))
print(f.getvalue())