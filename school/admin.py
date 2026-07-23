from django.contrib import admin
from school.models import School, Student, Subject,Grade
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['id','name']
    list_filter = ['id','name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['id']
    list_filter = ['id']




#for grade and subjects
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    autocomplete_fields = ['subject']

