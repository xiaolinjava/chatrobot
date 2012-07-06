'''
Created on 2012-7-4

@author: Administrator

@deprecated: Tuple 是不可变的 list。
@deprecated: 一旦创建了个 tuple，就不能以任何方式改变它。
@deprecated: Tuple 的元素与 list 一样按定义的次序进行排序。
@deprecated: 你不能够在tuple上进行append，extend，remove，pop，index的调用，因为他没有这些方法。
@deprecated: 但是你可以使用in来查看一个元素释放存在于tuple中。
@deprecated: tuple 比list操作速度要快，适用于一个值的常量集。
@deprecated: 如果你要不断的遍历集合，请首要的选择tuple代替list，前提是这个集合必须是一个常量值集。
@deprecated: tuple可以作为dictionary的key，但是list不能，前提是tuple中不包含list的元素
@deprecated: tuple 可以转换成list，反之亦然。
'''
t = ("aaaa", "bbbb", "cccc", "dddd", "eeee")

print(t)

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
'''
print(t[5])
'''

print(t.__class__)



#1.可以转换成list，反之亦然。
def make_list(t):
    l = []
    
    for e in t:
        l.append(e)
        
    return l


ll = make_list(t)
print("自定义函数将tuple转换成list：" ,ll)

#2.可以转换成list，反之亦然。
l = [e for e in t]
print("列表推导式(list comprehension)将tuple转换成list", l)


#3.可以转换成list，反之亦然。
ll = list(t)
print("内建函数将tuple转换成list：", ll)



t = tuple(ll)

print(t)


