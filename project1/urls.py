from django.urls import path
from .views import create_student,view_student

urlpatterns = [
    path('creat/', create_student, name='create_student'),
    path('view/',view_student, name="view_student"),
]