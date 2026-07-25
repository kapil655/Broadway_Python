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
    
    # ==================== FACULTY URLs ====================
    path('faculties/', views.view_faculties, name='view_faculties'),
    path('faculty/<int:faculty_id>/', views.faculty_detail, name='faculty_detail'),
    path('faculty/add/', views.add_faculty, name='add_faculty'),
    path('faculty/edit/<int:faculty_id>/', views.edit_faculty, name='edit_faculty'),
    path('faculty/delete/<int:faculty_id>/', views.delete_faculty, name='delete_faculty'),
    
    # ==================== SUBJECT URLs ====================
    path('subjects/', views.view_subjects, name='view_subjects'),
    path('subject/add/', views.add_subject, name='add_subject'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('subject/edit/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('subject/delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    
    # ==================== GRADE URLs ====================
    path('grades/', views.view_grades, name='view_grades'),
    path('grade/add/', views.add_grade, name='add_grade'),
    path('grade/<int:grade_id>/', views.grade_detail, name='grade_detail'),
    path('grade/edit/<int:grade_id>/', views.edit_grade, name='edit_grade'),
    path('grade/delete/<int:grade_id>/', views.delete_grade, name='delete_grade'),
    
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