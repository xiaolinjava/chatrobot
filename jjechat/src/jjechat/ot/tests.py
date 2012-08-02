#!/usr/bin/python
# _*_ coding: utf-8 _*_
'''
Created on 2012-7-24

@author: Administrator
'''


from django import template

def youName(name):
    
    c = template.Context({'name': name})
    t = template.Template('My name is {{name}}.')

    return t.render(c)

print(youName("xiaocilin"))


from django.template import Context, Template

def yourName(name):
    c = Context({'name': name})
    t = Template('My name is {{name}}.')
    return t.render(c)

print(yourName('xiaolin'))




raw_template = """ 
    <p>Dear {{person_name}},</p>
    <p>
        Thanks for placing an order from {{company}}. It's scheduled to ship on {{ ship_date|date:"F j, Y"}}.
    </p>
    {% if ordered_warranty %}
    <p>Your warranty information will be included in the packaging.</p>
    {% else %}     
    <p>
        Your didn't order a warranty, so you're on your own when the products inevitably stop working.
    </p>
    {% endif %}
    <p>Sincerely, <br /> {{company}}</p>
"""
t = Template(raw_template)
import datetime
c = Context({'person_name': 'John Smith',  
             'company': 'Outder Equipment', 
             'ship_date': datetime.date(2012, 7, 23), 
             'ordered_warranty': False
})


print(t.render(c))


#Bad
for name in ('John', 'Julie', 'Pat'):
    t = Template('Hello, {{name}}')
    print(t.render(Context({'name': name})))


#Good
t = Template('Hello, {{name}}')
for name in ('John', 'Julie', 'Pat'):
    print(t.render(Context({'name': name})))


person = {'name': 'Sally', 'age': '25'}
t = Template('{{person.name}} is {{person.age}} years old.')
c = Context({'person': person})

print(t.render(c))


from django.template import Template, Context

import datetime

d = datetime.date(1993, 5, 2)
print(str(d.year) +"-"+ str(d.month) +"-"+ str(d.day))

t = Template('The month is {{date.month}} and the year is {{date.year}}.')
c = Context({'date': d})
print(t.render(c))



#class
class Person(object):
    
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
    
t = Template('Hello, {{person.first_name}} {{person.last_name}}.')
c = Context({'person': Person('John', 'Smith')})
print(t.render(c))


t = Template('{{var}} -- {{var.upper}} -- {{var.isdigit}}')
c = Context({'var': 'hello'})
print(t.render(c))
 
c = Context({'var': '222'})
print(t.render(c))



t = Template('Item 2 is {{ item.2}}.')
c = Context({'item': ['apples', 'bananas', 'carrots']})
print(t.render(c))




t = template.Template('Your name is {{name}}.')
print(t.render(Context()))


c = Context({'foo': 'bar'})
print(c['foo'])


#反向迭代：{% for athlete in athlete_list reversed %}



















