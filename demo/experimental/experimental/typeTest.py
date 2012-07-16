#!/usr/bin/python
# -*- coding: utf-8 -*-

import dictionaryTest

import types


#type函数返回任意对象的数据类型
print(type(1))

print(type(dictionaryTest))

print(type([]))

print(type(""))


print(type(dictionaryTest) == types.ModuleType)

print(type(dictionaryTest) == types.MethodType)

