#!/usr/bin/python
# -*- coding: utf-8 -*-

import dictionaryTest


#使用getattr函数，可以得到一个直到运行时才知道名称的函数的引用。
li = ["Larry", "curly"]

print(li.pop)

print(getattr(li, "pop"))

print(getattr({}, "clear"))

#返回值是方法的话，这样等同于调用list的append方法，添加一个参数
getattr(li, "append")("Moe")

print(li)

#print(type(getattr(li, "pop")))


print(dictionaryTest.buildConnectionString)

print(getattr(dictionaryTest, "buildConnectionString"))

print(type(getattr(dictionaryTest, "buildConnectionString")))

