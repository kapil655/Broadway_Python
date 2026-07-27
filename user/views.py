from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse
from user.models import UserImage

# Create your views here.


def user_view(request):
    return HTTPResponse("this is from user")

def UserImage(request):
    return ()