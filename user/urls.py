from django.urls import path

from user.views import register,login_user

urlpatterns =[
   path('register/', register, name='user-register'),
   path("login/", login_user, name="user-login"),


]