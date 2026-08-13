from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student
from .forms import StudentForm



class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_create.html"
    success_url = reverse_lazy("student_list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_update.html"
    success_url = reverse_lazy("student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = reverse_lazy("student_list")


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"
    context_object_name = "student"

