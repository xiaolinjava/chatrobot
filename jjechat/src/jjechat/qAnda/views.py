from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'qAnda/index.html')

@csrf_exempt  
def talk(request):
    print request.POST['question']
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), mimetype="application/json") 
    