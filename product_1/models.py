from django.db import models

# Create your models here.
class show_product(models.Model):
    name = models.CharField(max_length=20, blank=False , null= False, help_text="enter your name")
    address = models.CharField(max_length=20, blank=False , null= False, help_text="enter your address")
    number = models.PositiveBigIntegerField(blank=False , help_text="enter your phone number")
    parentName = models.CharField(max_length=20, blank=False, null=False, help_text="enter your parent name: ")



    
    
