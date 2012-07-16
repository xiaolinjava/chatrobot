#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2012-7-11

@author: Administrator
'''
#dir 函数返回任意对象的属性和方法列表

import dictionaryTest


def _dir(object) :
    return dir(object)

li = []
print(_dir(li))

dict = {}
print(_dir(dict))


print(_dir(dictionaryTest))

print(_dir(""))

