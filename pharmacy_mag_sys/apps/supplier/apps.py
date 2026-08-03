from django.apps import AppConfig


class SupplierConfig(AppConfig):  # Changed from MedicineConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.supplier'