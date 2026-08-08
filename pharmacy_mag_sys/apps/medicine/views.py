from django.views.generic import (CreateView,ListView,DeleteView,DetailView,UpdateView)

from apps.medicine.forms import MedicineForm
from apps.medicine.models import Medicine


class MedicineList(ListView):
    model = Medicine
    template_name = "medicine/list.html"
    context_object_name = "medicines"


class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = "medicine/create.html"
    success_url = "/medicine/list"


class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = "medicine/update.html"
    success_url = "/medicine/list"


class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = "medicine/delete.html"
    success_url = "/medicine/list"


class MedicineDetailView(DetailView):
    model = Medicine
    template_name = "medicine/detail.html"
    context_object_name = "medicine"