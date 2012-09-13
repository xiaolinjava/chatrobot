#!/usr/bin/python
# _*_ coding: utf-8 _*_

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from jjechat.qAnda.models import QAndA
import json


def home(request):
    return render(request, 'qAnda/index.html')

@csrf_exempt  
def talk(request):
    question=request.POST['question'].strip("\r\n")
    sq=request.POST['sq'].strip("\r\n")   
    response_data = {}  
    if sq:
       QAndA(question=sq,answer=question).save()
    else:     
        try: 
            qAndaList=QAndA.objects.filter(question=question)       
            response_data['result'] = 'failed'
            response_data['message'] = 'You must add one'
            if qAndaList.__len__()!=0:        
                response_data['result'] = "\r\n我 :"+question+"\r\n小美:"+qAndaList[0].answer
                response_data['message'] = '' 
            else :
                response_data['result'] = '\r\n我 :'+question
        except  Exception,e:  
            print e     
    return HttpResponse(json.dumps(response_data), mimetype="application/json") 
    