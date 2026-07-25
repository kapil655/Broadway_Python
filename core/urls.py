
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('project1/', include('project1.urls')),
   path('school/', include('school.urls')), 
   path('product1/',include('product_1.urls')),
    
    
]