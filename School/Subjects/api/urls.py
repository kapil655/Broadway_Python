from django.urls import path
from .views import (
    SubjectListView, SubjectCreateView, SubjectDetailView,
    SubjectUpdateView, SubjectDeleteView
)

urlpatterns = [
    path('', SubjectListView.as_view()),
    path('create/', SubjectCreateView.as_view()),
    path('<int:id>/', SubjectDetailView.as_view()),
    path('<int:id>/update/', SubjectUpdateView.as_view()),
    path('<int:id>/delete/', SubjectDeleteView.as_view()),
]