from django.urls import path
from .views import (
    SubjectListView,
    SubjectCreateView,
    SubjectUpdateView,
    SubjectDeleteView,
    SubjectDetailView,
)

urlpatterns = [
    path("", SubjectListView.as_view(), name="subject_list"),
    path("create/", SubjectCreateView.as_view(), name="subject_create"),
    path("<int:pk>/", SubjectDetailView.as_view(), name="subject_detail"),
    path("update/<int:pk>/", SubjectUpdateView.as_view(), name="subject_update"),
    path("delete/<int:pk>/", SubjectDeleteView.as_view(), name="subject_delete"),
]