from django.urls import path
from apps.pharmacy.api.views import PharmacyView

urlpatterns = [
    path('', PharmacyView.as_view()),
    
]