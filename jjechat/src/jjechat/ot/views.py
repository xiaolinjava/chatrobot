#!/usr/bin/python
# _*_ coding: utf-8 _*_
'''
Created on 2012-7-18

@author: Administrator
'''
from django.http import HttpResponse, Http404

import datetime
from compiler.ast import For

def index(request, offset=1):
    
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset) 
    #assert False
    html = "<html> \
                <body>\
                    In %s hour(s), it will be %s.\
                </body>\
            </html>" % (offset, dt)
            
    return HttpResponse(html)



def hello(request):
    return HttpResponse("Hello world!")






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






















































