#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  requests
r=requests.get("http://www.baidu.com")
print(r.cookies['BDORZ'])
# print(r.cookies['Cookie'])
# print(r.headers)
# header=r.headers
# for i in header.items():
#     print(i[0],i[1])
# r=r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print(r.text)
# print(r.url)
# print(r.encoding)
# print(r.content)#无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
'''
requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：

>>> r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
>>> r.json()
{'query': {'count': 1, 'created': '2017-11-17T07:14:12Z', ...
需要传入HTTP Header时，我们传入一个dict作为headers参数：

>>> r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
>>> r.text
'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n <title>豆瓣(手机版)</title>...'
'''
# with open("E:\datanewend.xls",'rb') as filexcl:
#     if filexcl.readline() :
#         print(filexcl.readline())

'''
类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头
'''