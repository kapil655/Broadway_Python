from .views import create_student, view_student, delete_student
from django.urls import path

urlpatterns = [
    path("creat/", create_student, name="create-student"),
    path("view/", view_student, name="view-student"),
    path("delete/<int:id>/", delete_student, name="delete-student"),
]