from django.urls import path
from .views import (
    TeacherListView, TeacherCreateView, TeacherDetailView,
    TeacherUpdateView, TeacherDeleteView
)

urlpatterns = [
    path('', TeacherListView.as_view()),
    path('create/', TeacherCreateView.as_view()),
    path('<int:id>/', TeacherDetailView.as_view()),
    path('<int:id>/update/', TeacherUpdateView.as_view()),
    path('<int:id>/delete/', TeacherDeleteView.as_view()),
]