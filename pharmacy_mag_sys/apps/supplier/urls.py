from django.urls import path

from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
    SupplierDetailView,
)

urlpatterns = [
    path("list/", SupplierListView.as_view(), name="supplier-list"),

    path("create/", SupplierCreateView.as_view(), name="supplier-create"),

    path("detail/<int:id>/",SupplierDetailView.as_view(),name="supplier-detail"),

    path("update/<int:id>/",SupplierUpdateView.as_view(),name="supplier-update"),

    path("delete/<int:id>/",SupplierDeleteView.as_view(),name="supplier-delete"),
]