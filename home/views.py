from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    data = request.GET
    name = data.get('name','default')    
    return HttpResponse(name)


def Json_data(request):
    data = {
        "name\n ":"kapil",
        "age":34,
    }
    return JsonResponse(data)

 
