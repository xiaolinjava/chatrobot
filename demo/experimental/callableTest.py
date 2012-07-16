#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-7-11

@author: Administrator
'''

#callable 函数接收任何对象作为参数，如果参数对象是可调用的，返回True，否则返回False
#可调用对象包括函数，类方法，甚至类自身

import string
from zx import info

print(string.punctuation)


print(str.join)

#函数
print(callable(str))#True

#类自身
print(callable(list)) #True

#类方法
print(callable(list.append)) #True

#模型属性不可调用
print(callable(string.punctuation))#False

#模型类型不可调用
print(callable(string))#False


#type str，dir 以及其他python内置函数都归到__builtin__这个特殊的模块中
#默认python会在启动时自动执行【from __builtin__ import * 】
#所有在这个命名空间中可以直接使用这些内置函数
#from __builtin__ import *  #将所有的内置函数导入该命名空间































