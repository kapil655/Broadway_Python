from django.urls import path

from apps.medicine.views import (
    MedicineList,
    MedicineCreateView,
    MedicineUpdateView,
    MedicineDeleteView,
    MedicineDetailView,
)


urlpatterns = [
    path("list", MedicineList.as_view(), name="medicine-list"),
    path("create", MedicineCreateView.as_view(), name="medicine-create"),
    path("update/<int:pk>",MedicineUpdateView.as_view(),name="medicine-update"),
    path("detail/<int:pk>",MedicineDetailView.as_view(),name="medicine-detail"),
    path("delete/<int:pk>",MedicineDeleteView.as_view(),name="medicine-delete"),

    
    
]