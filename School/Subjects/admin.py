# subjects/admin.py
from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'subject_name', 'class_name', 'teacher', 'is_active']
    list_filter = ['subject_type', 'is_active']
    search_fields = ['subject_code', 'subject_name']