from django.urls import path
from home.views import home,Json_data

urlpatterns =    [
    path('data/', home),
    path('json/',Json_data),

]