#!usr/bin/python
# _*_ coding: utf-8 _*_
'''
Created on 2012-7-13

@author: Administrator
'''

#过滤list
li = ["a", "foo", "b", "c", "d", "dd", "bb"]

print(li)
#len 为内置函数
filteredLi = [elem + "abc" for elem in li if len(elem) > 1]
print(filteredLi)



filteredLi = [elem for elem in li if len(elem) == 1]
print(filteredLi)


filteredLi = [elem + "abc" for elem in li if elem == 'bb']
print(filteredLi)

#count是一个列表的方法，返回某个值在列表中出现的次数
filteredLi = [elem for elem in li if li.count(elem) == 1]
print(filteredLi)



