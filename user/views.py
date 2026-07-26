from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def user_view(request):
    return HTTPResponse("this is from user")