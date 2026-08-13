from urllib import request

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User
from .forms import UserForm


class UserListView(ListView):
    model = User
    template_name = "list.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "create.html"
    success_url = reverse_lazy("list")


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "update.html"
    success_url = reverse_lazy("list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("list")

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            from Teacher.models import Teacher
            from Students.models import Student
            
            context['total_users'] = User.objects.count()
            context['total_teachers'] = Teacher.objects.count()
            context['total_students'] = Student.objects.count()
            context['recent_users'] = User.objects.all().order_by('-created_at')[:5]
            context['recent_teachers'] = Teacher.objects.all().order_by('-id')[:5]
            context['recent_students'] = Student.objects.all().order_by('-id')[:5]
        except ImportError:
            context['total_users'] = 0
            context['total_teachers'] = 0
            context['total_students'] = 0
            context['recent_users'] = []
            context['recent_teachers'] = []
            context['recent_students'] = []
        
        return context
class LoginView(DjangoLoginView):
    template_name ="login.html"


