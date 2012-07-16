#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2012-7-11

@author: Administrator
@deprecated:  str 字符串函数
'''
import zx
import types

#str 将数据强制转换为字符串。每种数据类型都可以强制转换为字符串。
print(type(str(1)))

horsemen = ["war", "pestilence", "famine"]

horsemen.append("Powerbuilder")

print(type(str(horsemen)))

print(zx)

print("zx type is " + str(type(zx)))

print(None)

print(type(str(None)))

print(str(None) == 'None')

print(None == 'None')

