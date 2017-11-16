#! /user/bin/env python3
# -*- coding:utf-8 -*-
'''
class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
'''
class Student(object):
    #注意：特殊方法“init”前后有两个下划线！！！
    #注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self,name,code):
        self.name=name
        self.code=code

    def other_function(self,name,code):
        self.hehe="baidu"#任何地方植入变量
        print(name,code)
        return "谢谢使用"
var=Student('lilang','89')
print(var.other_function(var.name,var.code))
print(var.hehe)
