from django.urls import path
from .views import (
    CustomerListView, 
    CustomerCreateView, 
    CustomerDetailView,
    CustomerUpdateView, 
    CustomerDeleteView
)

app_name = 'customer'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
]

# from django.urls import path
# from customer.views import CustomerDetailView, CustomerList,CustomerCreateView,CustomerUpdateView,CustomerDeleteView

# urlpatterns = [
#     path('list', CustomerList, name='customer_list'),
#     path('create/', CustomerCreateView, name='customer_create'),
#     path('<int:pk>/', CustomerDetailView, name='customer_detail'),
#     path('update/<int:pk>/', CustomerUpdateView, name='customer_update'),
#     path('delete/<int:pk>/', CustomerDeleteView, name='customer_delete'),
# ]