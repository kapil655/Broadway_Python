from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib import messages
from django.db import models

from apps.customer.forms import CustomerForm
from apps.customer.models import Customer

# Create your views here.

class CustomerListView(ListView):
    model = Customer
    template_name = "customer/list.html"
    context_object_name = "customers"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        status_filter = self.request.GET.get('status')
        
        if search:
            queryset = queryset.filter(
                models.Q(full_name__icontains=search) |
                models.Q(phone__icontains=search) |
                models.Q(email__icontains=search)
            )
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['status_filter'] = self.request.GET.get('status', '')
        return context

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/create.html'
    success_url = reverse_lazy('customer:customer_list')

    def form_valid(self, form):
        messages.success(self.request, f'Customer {form.instance.full_name} created successfully!')
        return super().form_valid(form)

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customer/delete.html"
    success_url = reverse_lazy('customer:customer_list')

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        customer_name = customer.full_name
        messages.success(self.request, f'Customer {customer_name} deleted successfully!')
        return super().delete(request, *args, **kwargs)

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/update.html"
    success_url = reverse_lazy('customer:customer_list')

    def form_valid(self, form):
        messages.success(self.request, f'Customer {form.instance.full_name} updated successfully!')
        return super().form_valid(form)

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customer/detail.html"
    context_object_name = "customer"

# from django.shortcuts import render
# from django.views.generic import CreateView, ListView,DeleteView, TemplateView, UpdateView

# from apps.customer.forms import CustomerForm
# from apps.customer.models import Customer

# # Create your views here.

# class CustomerList(ListView):
#     model = Customer
#     template = "customer/list.html"
#     context_object_name = "customer"

# class CustomerCreateView(CreateView):
#     model = Customer
#     form_class = CustomerForm
#     template_name = 'customer/create.html'
#     success_url = "/customer.list"

# class CustomerDeleteView(DeleteView):
#     model = Customer
#     template_name = "customer/delete.html"
#     success_url = "/customer/list.html"

# class CustomerUpdateView(UpdateView):
#     model = Customer
#     form_class = CustomerForm
#     template_name = "customer/update.html"
#     success_url = "/customer/list"

# class CustomerDetailView(TemplateView):
#     model = Customer
#     template_name = "medicine/detail.html"
#     context_object_name = "customer"

    


     
    

