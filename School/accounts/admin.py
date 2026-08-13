from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "role", "phone_number", "is_verified", "created_at"]
    list_display_links = ["id", "name"]
    list_filter = ["role", "gender", "is_verified"]
    search_fields = ["name", "phone_number", "address"]
    list_editable = ["role", "is_verified"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    
    fieldsets = (
        ("Personal Info", {
            "fields": ("name", "gender", "date_of_birth")
        }),
        ("Contact", {
            "fields": ("phone_number", "address")
        }),
        ("Role & Status", {
            "fields": ("role", "is_verified")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
    
    actions = ["verify_users", "unverify_users"]
    
    @admin.action(description="Verify selected users")
    def verify_users(self, request, queryset):
        count = queryset.update(is_verified=True)
        self.message_user(request, f"{count} users verified.")
    
    @admin.action(description="Unverify selected users")
    def unverify_users(self, request, queryset):
        count = queryset.update(is_verified=False)
        self.message_user(request, f"{count} users unverified.")

admin.site.site_header = "School Management"    