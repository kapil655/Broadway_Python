from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # ==================== MAIN PAGES ====================
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    
    # ==================== SCHOOL URLs ====================
    path('schools/', views.view_schools, name='view_schools'),
    path('school/<int:school_id>/', views.school_detail, name='school_detail'),
    path('school/add/', views.add_school, name='add_school'),
    path('school/edit/<int:school_id>/', views.edit_school, name='edit_school'),
    path('school/delete/<int:school_id>/', views.delete_school, name='delete_school'),
    
    # ==================== TEACHER URLs ====================
    path('teacher/', RedirectView.as_view(pattern_name='view_teachers', permanent=False)),
    path('teachers/', views.view_teachers, name='view_teachers'),
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/add/', views.add_teacher, name='add_teacher'),
    path('teacher/edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    
    # ==================== STUDENT URLs ====================
    path('student/', RedirectView.as_view(pattern_name='view_students', permanent=False)),
    path('students/', views.view_students, name='view_students'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/add/', views.add_student, name='add_student'),
    
    # ==================== ATTENDANCE URLs ====================
    path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/report/', views.attendance_report, name='attendance_report'),
    
    # ==================== API / AJAX URLs ====================
    path('api/search-students/', views.search_students, name='search_students'),
]