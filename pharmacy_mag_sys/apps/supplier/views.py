from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Supplier


class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier/list.html"
    context_object_name = "suppliers"


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "supplier/add.html"
    fields = [
        "company_name",
        "contact_person",
        "email",
        "phone",
        "registration_num",
        "address",
        "payment_terms",
        "status",
    ]
    success_url = reverse_lazy("supplier-list")


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "supplier/detail.html"
    context_object_name = "supplier"


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "supplier/add.html"
    fields = [
        "company_name",
        "contact_person",
        "email",
        "phone",
        "registration_num",
        "address",
        "payment_terms",
        "status",
    ]
    success_url = reverse_lazy("supplier-list")


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier/delete.html"
    success_url = reverse_lazy("supplier-list")