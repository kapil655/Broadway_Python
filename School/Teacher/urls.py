from django.urls import path
from .views import (
    TeacherListView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView,
    TeacherDetailView,
)

urlpatterns = [
    path("", TeacherListView.as_view(), name="teacher_list"),
    path("create/", TeacherCreateView.as_view(), name="teacher_create"),
    path("<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("update/<int:pk>/", TeacherUpdateView.as_view(), name="teacher_update"),
    path("delete/<int:pk>/", TeacherDeleteView.as_view(), name="teacher_delete"),
]