from django.contrib import admin
from school.models import School, Student
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

