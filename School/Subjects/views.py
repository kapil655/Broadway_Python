# subjects/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Subject
from .forms import SubjectForm


class SubjectListView(ListView):
    model = Subject
    template_name = "subject_list.html"
    context_object_name = "subjects"


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject_create.html"
    success_url = reverse_lazy("subjects:subject_list")  # ✅ Added 'subjects:' namespace


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject_update.html"
    success_url = reverse_lazy("subjects:subject_list")  # ✅ Added 'subjects:' namespace


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "subject_delete.html"
    success_url = reverse_lazy("subjects:subject_list")  # ✅ Added 'subjects:' namespace


class SubjectDetailView(DetailView):
    model = Subject
    template_name = "subject_detail.html"
    context_object_name = "subject"