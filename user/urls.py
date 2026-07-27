from django.urls import path
from user.views import user_view

urlpatterns =[
    path('view',user_view,name="view")
]