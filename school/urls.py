from django.urls import path
from school.views import grade_delete, grade_list, grade_update, student_list ,student_create,student_update,student_delete,grade_create

urlpatterns = [
    path('student', student_list , name="student"),
    path('student-create', student_create , name="student-create"),
    path('student-update/<int:id>', student_update , name="student-update"),
    path('student-delete/<int:id>', student_delete , name="student-delete"),
    path('student-update/<int:id>',student_update, name="student-update"),

    #grade-data-link 
    path("grade-list/", grade_list, name="grade-list"),
    path('grade-create/',grade_create, name="grade-create"),
    path('grade-update/<int:id>',grade_update, name="grade-update"),
    path('grade-delete/<int:id>',grade_delete, name="grade-delete"),

]