#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
try:
    11/0
except BaseException as e:
    print(e)
else:
    print("没有异常")
finally:
    print("finally")
try:
    f=open("E:\data\sdnetdata\python\scenic\data.txt",encoding='utf-8')
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(1)
            print("hello"+content)
    except BaseException as e:
        print(e)
    finally:
        f.close()
        print("关闭文件")
except FileNotFoundError:
    print("没有这个文件")