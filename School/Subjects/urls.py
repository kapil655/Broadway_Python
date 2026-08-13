from django.urls import path
from .views import (
    SubjectListView,
    SubjectCreateView,
    SubjectUpdateView,
    SubjectDeleteView,
    SubjectDetailView
)

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
    path('create/', SubjectCreateView.as_view(), name='subject_create'),
    path('<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
]