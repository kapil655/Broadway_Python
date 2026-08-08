# apps/pharmacy/api/urls.py
from django.urls import path
from .views import PharmacyListView, PharmacyCreateView, PharmacyUpdateView, PharmacyDeleteView

urlpatterns = [
    path('list/', PharmacyListView.as_view(), name='pharmacy-list'),
    path('create/', PharmacyCreateView.as_view(), name='pharmacy-create'),
    path('update/<int:id>/', PharmacyUpdateView.as_view(), name='pharmacy-update'),
    path('delete/<int:id>/', PharmacyDeleteView.as_view(), name='pharmacy-delete'),
]