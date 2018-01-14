#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def test(number):
    print("*"*20)
    def testMore():
        print("#"*20)
    print("test end"+"*"*20)
    return testMore
test(100)()