#!/usr/bin/python
# _*_ coding: utf-8 _*_
'''
Created on 2012-7-18

@author: Administrator
'''
from django.http import HttpResponse, Http404
from django.template import Template, Context

import datetime

'''
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
    now = datetime.datetime.now()
    t = Template("""
        <html>
            <body>
                <font style='color:red;'>
                    hello world！！
                </font>
                It is now <font style='color:red;'>{{current_date}}</font>.
            </body>
        </html>
        """)
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


'''
from django.shortcuts import render_to_response


#def index(request, offset=1):
#    now = datetime.datetime.now()
#    return render_to_response('index.html', {'current_date': now}) 
def index(request, offset=1):
    current_date = datetime.datetime.now()
    return render_to_response('index.html', locals()) 



from django.template.loader import get_template

def hello(request):
    now = datetime.datetime.now()
    t = get_template('hello.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


from django.db import  connection

cursor = connection.cursor()
print(cursor)















































