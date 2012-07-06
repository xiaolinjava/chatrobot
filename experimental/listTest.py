'''
Created on 2012-7-3

@author: Administrator
'''

li = ["aaaa", "bbbb", "cccc", "dddd", "eeee"]

print(li)

'''根据list的小标获得list元素 ''' 
print(li[0])

'''根据指定元素获得list的下标 '''
print(li.index("dddd", ))

''' 静态插入指定下标的元素到list中'''
li.insert(5, "ffff")
print(li)

'''动态的往list元素中插入数据 '''
li.append("gggg")
print(li)

li.append("gggg")
print(li)

li.remove("gggg")
print(li)

if li.__contains__("gggg"):
    print("I hava gggg........")
else:
    print("I havn't gggg....")
    
'''获得list元素的长度 '''
print(li.__len__())

print(li.__doc__)


''' python中支持list数组的负数下标检索，等同于倒数检索，但是倒数下标是从1开始，而不是从0开始'''
''' li[-n] == li[len(li) - n]'''
print(li[-1])

print(li[-2])


'''将list的数组元素倒排序 '''
li.reverse()
print(li)

'''通过指定 您可以通过指定 您可以通过指定 2 个索引得到  list 的子集，叫做一个 “ “slice”, 专业术语叫list的分片 '''
''' 简单的可以理解为java中list的subList方法'''
print(li[0:3])

print(li[0:-1])

print(li[-1:0])
print(li[-1:1])
print(li[-1:2])
print(li[-1:3])


'''简写形式 '''
print(li[:3])

print(li[3:])

'''这样是一个新的list '''
newLi = li[:]
print(newLi)

''' extend 连接newLi到li中，将后一个list连接到前一个list中'''
li.extend(newLi)

''' 与extend不一样，append是将后一个list作为前一个list的元素加入'''
li.append(newLi)


print(li)


''' index在list中查找一个值首次出现并返回索引值'''
print(li.index("aaaa"))


'''如果在list中查找不到一个值，则会抛异常
print(li.index("d"))
'''

'''
检测一个值是否在list中，可以使用in 
'''
if "aaaa" in li:
    print("I is li element")
else:
    print("I isn't li element") 
    


if ("aaa" == True) :
    print("aaa is true")
else:
    print("aaa is false")
    

if ("aaa"):
    print("aaa is true")
else:
    print("aaa is false")
    

'''删除list的最后的一个元素，返回删除的这个元素 '''
print(li.pop())

print(li)

li += newLi
print(li)

''' 
list的+ 号连接符与extend的不同地方在于，前者或返回一个新的list，二后者只是改变list的元素，不返回新的list
所以，在大数据量的list连接的时候，extend的速度快
'''
ll = (li + newLi)*2
print(ll)











































