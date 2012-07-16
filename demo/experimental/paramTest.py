#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-7-9

@author: Administrator
@deprecated: Python 的变量跟java一样，但是python变量不需要定义，只需要赋值就可以，但是如果你引用一个为赋值的变量是非法的
'''
import dictionaryTest

#变量的赋值是一条被分成多行的命令，用反斜线（\）作为续行符，有续行符，可以不需要按照python缩进
myParams = {"server":"mpilgrim", \
        "database":"master", \
        "uid":"sa", \
        "pwd":"secret" \
        }

print(myParams)


#一次赋 多值
#v 是一个三元素的tuple，（x, y, z）是一个三变量的tuple
v = ("a", "b", "c")
print(v)

#将一个tuple赋值给另一个tuple，会按照顺序将v的每个值赋值给每个变量
(x, y, z) = v
print(x, y, z)



#连续值 赋值 range函数
#内置的range函数返回一个元素为整数的list
#range函数的调用形式是接收一个上限值，返回一个初始值从0开始的list，他依次递增，知道但不包含上限值

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print((MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY))

#但是可以设置range的初始值不从0开始，如range(1, 8)
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(1, 8)
print((MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY))


print(range.__doc__)



#字符串的格式化,通过占位符的方式赋值格式化
k = "uid"
v = "sa"
print ("%s = %s" %(k, v))


#字符串的格式化不仅仅只是连接字符串，而且是强制类型转换

userCount = 6

print("Users connected: %d" %(userCount, ))


# 这里强制转换抛异常
#TypeError: Can't convert 'int' object to str implicitly
#print("Users connected: " + userCount)



#数值的格式化
#%f 格式符选项对应一个十进制浮点数，不指定精度时打印6位小数
print("Today's stock price: %f" %50.4625)
print("Today's stock price: %.2f" %50.4625)
print("Today's stock price: %+.2f" %50.4625)
print("Today's stock price: %+.2f" %-50.4625)




#映射 list

#python的强大特性之一是其对list的解析，他提供了一种紧凑的方法
#可以通过对list中的每一个元素应用一个函数，从而将list映射为另一个list

li = [1, 9, 8, 4]
#我们从右往左看，li是一个将要映射的list，python循环遍历li中的每个元素，对每个元素均指向如下操作：
#首先临时将其赋给遍历elem，而后python应用函数elem*2 进行计算，最后计算结果追加到要返回的list中
li = [elem*2 for elem in li]
print(li)



myParams = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
#dict_items([('pwd', 'secret'), ('database', 'master'), ('uid', 'sa'), ('server', 'mpilgrim')])
print() 

itemLi = myParams.items();
print("========itemLi=========")
print(itemLi)
print("=================")
li = ["%s==%s" %(k,v) for (k, v) in itemLi]
print("=================")
print(li)
print("=================")
print("  ".join(li))

li = ["%s=%s" %(k,v) for (k, v) in itemLi]

s = ";".join(li)
print(s)


k, v = ('pwd', 'secret')
print(k, v)

(k, v) = ('pwd', 'secret')
print(k,v)


print(li[2])


#字符串转list
l = s.split(";")

print(l)

#显示分割次数为1，可选参数
l = s.split(";", 1)
print(l)



#import调用其他模块的方法
li = dictionaryTest.buildConnectionString(myParams)
print(li)


params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}

li = ["%s==%s" %(k, v) for (k, v) in params.items()]
print(li)
li = [k for k, v in params.items()]
print(li)
li = [v for k, v in params.items()]

print(li)


























































