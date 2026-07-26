from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('project1/', include('project1.urls')),
    path('school/', include('school.urls')),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    