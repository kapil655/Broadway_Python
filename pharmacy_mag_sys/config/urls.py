
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/supplier/',include('apps.supplier.api.urls')),
    path('api/medicine/', include('apps.medicine.api.urls')),
     path('api/pharmacy/', include('apps.pharmacy.api.urls')),
]   
