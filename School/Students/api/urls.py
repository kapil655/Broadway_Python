from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view()),
    path('create/', StudentCreateView.as_view()),
    path('<int:id>/', StudentDetailView.as_view()),
    path('<int:id>/update/', StudentUpdateView.as_view()),
    path('<int:id>/delete/', StudentDeleteView.as_view()),
]