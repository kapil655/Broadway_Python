
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
#supplier
    path('supplier/',include('apps.supplier.urls')),
#medicine
    path('medicine/',include('apps.medicine.urls')),
#api-medicine
    path('api/medicine/', include('apps.medicine.api.urls')),
#api-supplier
    path('api/supplier/', include('apps.supplier.api.urls')),
#pharmacy
     path('pharmacy/', include('apps.pharmacy.urls')),
]
