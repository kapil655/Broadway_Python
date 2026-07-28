from http.client import HTTPResponse

from django.shortcuts import redirect, render
from django.http import HttpResponse
from user.models import UserImage
from user.forms import registerForm

# Create your views here.


def user_view(request):
    return HTTPResponse("this is from user")

def UserImage(request):
    return ()





def register(request):
   form = registerForm()
   context= {
       "form":form
   }
   return render(request , 'user/register.html', context)