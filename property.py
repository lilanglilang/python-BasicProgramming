#! user/bin/env python3
# -*- coding:utf-8 -*-
#非类的实现方式
class Score():
    __slots__ =('score')
    def setScore(self,score):
        if not isinstance(score,int):
            raise ValueError("对不起，你设置的值不是整数，重新设置！")#抛出异常后后面的值语句不在执行
        elif not 0<=score<=100:
            raise ValueError("对不起，您输入的值不在0到100内，请重新设置！")
        self.score=score
    def getScore(self):
       return self.score
myscore=Score()
# myscore.name='lilang' 错误的
#myscore.setScore(1000)#ValueError: 对不起，您输入的值不在0到100内，请重新设置！
myscore.setScore(10)

class Myproperty(object):
    @property
    def score(self):
        return self.google
    #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self,value):
        if not 0<=value<=100:
            print("您输入的数据有误！")
        self.google=value
demo=Myproperty()
demo.score=110
name=demo.score
print(name)
