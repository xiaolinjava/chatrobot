#!/usr/bin/python
# _*_ coding: utf-8 _*_
'''
Created on 2012-7-16

@author: Administrator
'''
#Python 支持一种有趣的语法，他允许你快速定义单行的最小函数。这些叫做lambda的函数，是从Lisp借用来的，可以用在任何需要函数的地方。
#相当于匿名函数
def f(x):
    return x*2


print(f(3))

g = lambda x: x*2
print(g(3))

print((lambda x: x*2)(3))

