from django.db import models
from django.contrib import admin

# Create your models here.
# class pharma_category(models.Model):
#     pharma_name = models.CharField(max_length=50 , verbose_name="Pharmacy Name")
#     pharma_address = models.CharField(max_length=50 , verbose_name="pharmacy Address")
#     pharma_number = models.PositiveIntegerField(max_length=10, verbose_name="Contact Number")
#     stock = models.BooleanField(default=True)
#     order_product = models.CharField(max_length=50 , verbose_name="order medicine")


#     def __str__(self):
#         return self.pharma_name

#     class Meta :
#         db_table = "pharmacy_detail"


class District(models.Model):
    district_id = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pharmacy(models.Model):
    name = models.CharField(max_length=50, verbose_name="Pharmacy_name")
    registration_number = models.PositiveIntegerField(blank=True)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    website = models.URLField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name="address")
    city = models.CharField(max_length=60, null=True, blank=True, verbose_name="city")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, verbose_name="District") 
    country = models.CharField(max_length=60, null=True, blank=True,verbose_name="country")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    status = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = "Pharmacy"

    def __str__(self):
        return self.name
