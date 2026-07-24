from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, help_text="Enter your name")
    address = models.CharField(max_length=30, blank=False, null=False, help_text="Enter your address")
    price = models.PositiveBigIntegerField(blank=True, null=True, help_text="Enter your product MRP.")
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"  # ✅ Better representation

    class Meta:
        db_table = "Product"