from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "teacher_id", "first_name", "last_name", "email", "phone_number"]
    list_display_links = ["id", "teacher_id"]
    list_filter = ["gender", "qualification"]
    search_fields = ["teacher_id", "first_name", "last_name", "email"]
    readonly_fields = ["teacher_id", "joining_date"]
    ordering = ["-id"]
    
    fieldsets = (
        ("Personal", {"fields": ("teacher_id", "first_name", "last_name", "gender", "date_of_birth")}),
        ("Contact", {"fields": ("email", "phone_number")}),
        ("Professional", {"fields": ("qualification", "specialization", "experience_years", "joining_date")}),
    )