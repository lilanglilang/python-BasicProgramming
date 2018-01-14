#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Game(object):
    num=0
    def __init__(self):
        self.name='ulike'
        self.num=1000
    @classmethod
    def addCls(cls):
        cls.num=100
    @staticmethod
    def staticMethod():
        print("static")
game=Game()
Game.addCls()
#print(game.num)
#1000
#print(Game.num)
#100
print(Game.staticMethod())
print(game.staticMethod())
