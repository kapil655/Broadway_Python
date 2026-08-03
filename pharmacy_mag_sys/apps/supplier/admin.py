from django.contrib import admin
from apps.supplier.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # Columns displayed in the admin list page
    list_display = (
        "id",
        "company_name",
        "contact_person",
        "email",
        "phone",
        "registration_num",
        "payment_terms",
        "status",
        "created_at",
        "updated_at",  # Added for consistency with list_filter
    )

    # Search bar
    search_fields = (
        "company_name",
        "contact_person",
        "email",
        "registration_num",
    )

    # Filters on the right sidebar
    list_filter = (
        "status",
        "created_at",
        "updated_at",
    )

    # Default ordering
    ordering = ("company_name",)

    # Number of records per page
    list_per_page = 20

    # Editable fields from the list page
    list_editable = ("status",)

    # Clicking these fields opens the detail page
    list_display_links = ("company_name",)

    # Read-only fields
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # Group fields on the edit page
    fieldsets = (
        ("Supplier Information", {
            "fields": (
                "company_name",
                "contact_person",
                "email",
                "phone",
            )
        }),
        ("Business Details", {
            "fields": (
                "registration_num",
                "address",
                "payment_terms",
                "status",
            )
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )