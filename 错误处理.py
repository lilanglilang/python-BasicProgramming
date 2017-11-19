#！user/bin/env python3
# -*- coding:utf-8 -*-
'''
Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

https://docs.python.org/3/library/exceptions.html#exception-hierarchy
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''
def function(a):
    if a==-1:
        print("hello")
    else:
        return "null"
function(-1)
print(function(2))
'''
try机制
'''
def myTry():
    try:
     1/0
    except Exception as  e:
        print(e)
myTry()#division by zero
def myTryTwo():
    try:
     1/0
    except Exception as  e:
        print(e)
    print("hello i still run")
myTryTwo()
#division by zero
#hello i still run
def myTryThree():
    try:
     1/0
     print("i will not run")
    except Exception as  e:
        print(e)
    print("hello i still run")
myTryThree()
#division by zero
#hello i still run
def myTryFour():
    try:
     1/0
     print("i will not run")
    except Exception as  e:
        print(e)
    finally:
        print("i will run anyway!")
    print("hello i still run")
myTryFour()
'''
division by zero
i will run anyway!
hello i still run
'''
def myTryFour():
    try:
     1/2
     print("there is not exception，i will run")
    except FileExistsError as  e:#随便列举的列子
        print(e)
    except ValueError as ve:
        print("数值错误")
    else:
        print("哇，竟然没错")
    finally:
        print("i will run anyway!")
    print("hello i still run")
myTryFour()
'''
there is not exception，i will run
哇，竟然没错
i will run anyway!
hello i still run
'''
#错误的记录
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了
# 既然我们能捕获错误，就可以把错误堆栈打印出来，
# 然后分析错误原因，同时，让程序继续执行下去。
import logging
def reallyE():
    for i in  range(1,10):
        try:
           print(i)
           1 / 0
        except BaseException as  bEx:
            logging.log(bEx)
reallyE()
print("你好")
'''
因为错误是class，捕获一个错误就是捕获到该class的一个实例。
因此，错误并不是凭空产生的，而是有意创建并抛出的。
Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
'''
class FooError(ValueError):
   pass
def foo(s):
    n=int(s)
    if n==0:
        raise FooError("错误信息")
def exception():
    try:
        10/0
    except ValueError as e:
        print(e)
        raise



