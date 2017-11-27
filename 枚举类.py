#！user/bin/env python3
# -*- coding:utf-8 -*-
'''
定义常量可以用大写字母代替
或者用枚举类型
更好的方法是为这样的枚举类型定义一个class类型，
每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
'''
from  enum import Enum,unique
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name,member)
for value in Month._member_names_:
    print(value)
@unique
class WeekDays(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(WeekDays(1))