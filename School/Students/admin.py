from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "student_id", "get_full_name", "class_name", "roll_number", "phone_number", "is_active"]
    list_display_links = ["id", "student_id", "get_full_name"]
    list_filter = ["class_name", "section", "gender", "is_active"]
    search_fields = ["student_id", "first_name", "last_name", "email", "phone_number"]
    list_editable = ["is_active"]
    readonly_fields = ["student_id", "admission_date", "created_at", "updated_at"]
    ordering = ["-created_at"]
    
    fieldsets = (
        ("Personal Information", {
            "fields": ("student_id", "first_name", "last_name", "gender", "date_of_birth")
        }),
        ("Contact Information", {
            "fields": ("email", "phone_number", "address")
        }),
        ("Parent Information", {
            "fields": ("parent_name", "parent_phone", "parent_email")
        }),
        ("Academic Information", {
            "fields": ("class_name", "section", "roll_number", "admission_date")
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = "Full Name"