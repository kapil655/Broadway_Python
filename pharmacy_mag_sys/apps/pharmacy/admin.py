from django.contrib import admin
from apps.pharmacy.models import District, Pharmacy

# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district_id', 'name']
    search_fields = ['name']
    ordering = ['district_id']

class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_number', 'email', 'phone', 'district', 'city', 'status']
    list_filter = ['status', 'district', 'city']
    search_fields = ['name', 'registration_number', 'email', 'phone']
    ordering = ['name']
    date_hierarchy = "created_at"
    
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'registration_number', 'email', 'phone', 'website')
        }),
        ('Location Details', {
            'fields': ('address', 'city', 'district', 'country')
        }),
        ('Timing', {
            'fields': ('opening_time', 'closing_time')
        }),
        # Removed the incorrectly formatted Medicine Information section
        # If you want to add Medicine information, you need to create a Medicine model first
        # and use inline admin
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Register models with admin
admin.site.register(District, DistrictAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)