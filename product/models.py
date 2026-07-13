from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, help_text="Enter your name")
    address = models.CharField(max_length=30, blank=False, null=False, help_text="Enter your address")
    number = models.PositiveBigIntegerField(blank=True, null=True, help_text="Enter your contact number")
    email = models.EmailField(blank=True, null=True)
    
  

# python manage.py makemigration
    class Meta:
        db_table="view_product"
