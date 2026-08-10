from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView,TemplateView,UpdateView,DeleteView,DetailView)
from django.db.models import Count

from apps.pharmacy import form
from apps.pharmacy.models import District, Pharmacy
from apps.pharmacy.form import PharmacyForm


class PharmacyListView(View):

    def get(self, request):
        pharmacies = Pharmacy.objects.all()
        context = {
            "pharmacies": pharmacies
        }

        return render(request,"pharmacy/list.html", context)


class PharmacyCreateView(CreateView):

    model = Pharmacy
    form_class = PharmacyForm
    template_name = "pharmacy/create.html"
    success_url = reverse_lazy("pharmacy_list")


class PharmacyUpdateView(UpdateView):

    model = Pharmacy
    form_class = PharmacyForm
    template_name = "pharmacy/create.html"
    success_url = reverse_lazy("pharmacy_list")


class PharmacyDeleteView(DeleteView):

    model = Pharmacy
    template_name = "pharmacy/delete.html"
    success_url = reverse_lazy("pharmacy_list")


class PharmacyDetailView(DetailView):

    model = Pharmacy
    template_name = "pharmacy/detail.html"
    context_object_name = "pharmacy"


class PharmacyDashboardView(TemplateView):

    template_name = "pharmacy/dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context.update({
            # Total pharmacies
            "total_pharmacies": Pharmacy.objects.count(),
            # Active pharmacies
            "active_pharmacies": Pharmacy.objects.filter(status=True).count(),
            # Inactive pharmacies
            "inactive_pharmacies": Pharmacy.objects.filter(status=False).count(),
            # Total districts
            "total_districts": District.objects.count(),
            # Recent pharmacies
            "recent_pharmacies": Pharmacy.objects.order_by("-created_at")[:5],
            # Pharmacies grouped by district
            "pharmacies_by_district": (District.objects.annotate(pharmacy_count=Count("pharmacy")).order_by("-pharmacy_count")),})

        return context