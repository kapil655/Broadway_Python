
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supplier/',include('apps.supplier.urls')),
    path('medicine/',include('apps.medicine.urls')),
    path('api/medicine/', include('apps.medicine.api.urls')),
     path('pharmacy/', include('apps.pharmacy.urls')),
]   
