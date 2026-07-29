from http.client import HTTPResponse

from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from user.models import UserImage
from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.


def user_view(request):
    return HTTPResponse("this is from user")

def UserImage(request):
    return ()

def register(request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return redirect("/")
        context = {"form": form}
        return render(request, "user/register.html", context)

def login_user(request):
     if request.user.is_authenticated:
          return redirect('/admin')
     form = LoginForm()
     if request.method == "POST":
          data = request.POST
          user = authenticate(request,username=data['username'],password=data['password'])
          if user is not None:
               login(request, user)
               return redirect("/")
          print(user)
     context = {"form": form}
     return render(request, "user/login.html", context)