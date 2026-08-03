from django.db import models

# Create your models here.
class Supplier(models.Model):
    company_name = models.CharField(max_length=50, help_text="Enter company name")
    contact_person = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)  # Changed from PositiveBigIntegerField
    registration_num = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    payment_terms = models.CharField(max_length=20, null=True, blank=True)
    status = models.BooleanField(default=True)  # Added default value
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Suppliers"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self) -> str:  
        return self.company_name