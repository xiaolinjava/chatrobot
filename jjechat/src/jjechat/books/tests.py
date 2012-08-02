#!/usr/bin/python
# _*_ coding: utf-8 _*_
from jjechat.books.models import Publisher

print("------------save----------------")
#insert(先创建对象，在插入数据库)
p1 = Publisher(name='Apress', address='2855 telegraph Avenue', city='Berkeley', state_province='CA', country='U.S.A', website='http://www.apress.com')
p1.save()

print("------------create----------------")
#insert(创建对象，同时插入数据库)
p2 = Publisher.objects.create(name="O'Reilly", address='10 Fawcett St.', city='Cambridge', state_province='MA', country='U.S.A', website='http://www.oreilly.com')

print("------------update----------------")
#update
p1.name = 'cilin.xiao'
p1.save()

print("-------------update----------")
count=Publisher.objects.filter(id=p1.id).update(name='Apress Publishing')
print(count)
p1 = Publisher.objects.order_by('name')[0]
print(p1)

print("-------------batch update----------")
count = Publisher.objects.all().update(city='USA')
print(count)

print("--------------delete--------------")
#delete
#p2 = Publisher.objects.all().delete()
#p2 = Publisher.objects.filter(country='USA').delete()



print("------------all----------------")    
publisher_list = Publisher.objects.all()
for pl in publisher_list :
    print(pl.name)

print("-------------order_by==all + order by name desc---------------")    
publisher_list_order_by = Publisher.objects.order_by('name')
for pl in publisher_list_order_by:
    print(pl.name)    
    
print("-------------order_by==all + order by name desc,address desc---------------")
publisher_list_order_by = Publisher.objects.order_by('name', 'address')
for pl in publisher_list_order_by:
    print(pl.name)  

print("----------逆向排序---order_by==all + order by name asc---------------")
publisher_list_order_by = Publisher.objects.order_by('-name')
for pl in publisher_list_order_by:
    print(pl.name)  

print("----------------select filter------------")    
#select
publisher_filter_list = Publisher.objects.filter(name="cilin.xiao")
for pl in publisher_filter_list :
    print(pl.name)

print("---------------select filter-------------")
#select any query condition
publisher_filter_list = Publisher.objects.filter(name="cilin.xiao", address='U.S').order_by('-name')
for pl in publisher_filter_list :
    print(pl.name)
    
print("-------------select filter contains---------------")
#select like query condition
publisher_filter_list = Publisher.objects.filter(name__contains="r")
for pl in publisher_filter_list :
    print(pl.name)
    
print("-------------select filter icontains---------------")
#select (大小写无关的LIKE) query condition
publisher_filter_list = Publisher.objects.filter(name__icontains="R")
for pl in publisher_filter_list :
    print(pl.name)

print("------------select get----------------")
#get query condition
try:
    p5 = Publisher.objects.get(name='bbb')
    print(p5)
except Publisher.DoesNotExist:
    print("Apress isn't in the database yet.")
else:
    print ("Apress is in the database.")

print("-------------select limit[0]----------")
p5 = Publisher.objects.order_by('name')[0]
print(p5)

print("-------------select limit[0:3]----------")    
p5 = Publisher.objects.order_by('name')[0:3]
for pl in p5:
    print(pl)
    
    
    

