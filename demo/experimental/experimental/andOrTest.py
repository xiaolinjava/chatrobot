#!/usr/bin/python
# _*_ coding: utf-8 _*_
'''
Created on 2012-7-16

@author: Administrator
'''
#0、''、[]、()、{}、None 在布尔环境中为假；其它任何东西都真。
#如果布尔环境中的所有值都为真，那么 and 返回最后一个值, or返回第一个为真的值。
#如果布尔环境中的某个值为假，则 and 返回第一个假值。
#如果布尔环境中所有的值都为假，则or返回最后一个为假的值。

flag = 0 and (1 or "a" or list)
print(flag)

flag = "" and (1 or "a" or list)
print(flag)


flag = [] and (1 or "a" or list)
print(flag)

flag = () and (1 or "a" or list)
print(flag)

flag = {} and (1 or "a" or list)
print(flag)

flag = 1 or "a" or list
print(flag)



a = ""
b = "abc"
#不安全的使用and-or组合 (bool ? a : b)
flag = 1 and a or b
print(flag)

#安全的使用and-or组合
flag = 1 and [a] or [b]


print(flag)
