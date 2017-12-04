#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned
    into uppercase.
  """
  print( "call upper_attr")


  # 除以__开头的属性外，其它属性转为大写
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # let `type` do the class creation
  return type(future_class_name, future_class_parents, uppercase_attr)


class Foo(object):
  __metaclass__ = upper_attr
  bar = 'bip'


print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
print(f.BAR)
# Out: 'bip'

'''
   Django的ORM就是这样干的，我们在Model中定义的字段类型是各种field类实例，但当创建该model类时，会将这些field类实例转为Python

内置的类型，如CharField()实例转为unicode或str类型，IntegerField()实例转为int型。

复制代码
# remember that `type` is actually a class like `str` and `int`
# so you can inherit from it
class UpperAttrMetaclass(type): 
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)
        元类可以做到：
        
        拦截类的生成
        修改类
        返回修改后的类
'''