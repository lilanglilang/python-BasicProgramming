#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = dict(name='Bob', age=20, score=88)
# print(d)
#{'name': 'Bob', 'age': 20, 'score': 88}
'''
我们把变量从内存中变成可存储或传输的过程称之为序列化 Python中叫pickling
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
只能用Pickle保存那些不重要的数据
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
并且可能不同版本的Python彼此都不兼容，
import pickle
# print(pickle.dumps(d))#方法把任意对象序列化成一个bytes
#pickle.dump()直接把对象序列化后写入一个file-like Object：
with open("hello.txt","ab") as files:
    pickle.dump(d,files)
fl=open("hello.txt","rb")
d=pickle.load(fl)
fl.close()
print(d)
'''

'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
JSON类型	Python类型
{}	           dict
[]      	    list
"string"	    str
1234.56 	    int或float
true/false	    True/False
null	        None

print("json**********************************")

d=dict(name='ll',company='google')
print(json.dumps(d))
dumps()方法返回一个str，内容就是标准的JSON。
类似的，dump()方法可以直接把JSON写入一个file-like Object。
with open('hello.txt','w') as  jsonfile:
    json.dump(json.dumps(d),jsonfile)
'''

'''
json进阶

'''
import  json
class student():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
s=student('bob','42','boy')
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'sex': std.sex
    }
print(json.dumps(s,default=student2dict))
#因为通常class的实例都有一个__dict__属性，它就是一个dict，
# 用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s,default=lambda obj:obj.__dict__))

#json转化为实体对象
def jsonToBean(obj):
    return student(obj['age'],obj['sex'],obj['name'])
json_str = '{"name": "Bob","age": 20, "sex": 88}'
print(json.loads(json_str,object_hook=jsonToBean))
'''
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例：
'''
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)#{"name": "小明", "age": 20}
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)#{"name": "\u5c0f\u660e", "age": 20}
'''
Python语言特定的序列化模块是pickle，
但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
json模块的dumps()和loads()函数是定义得非常好的接口的典范。
当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，
我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''