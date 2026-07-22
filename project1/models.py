from django.db import models


class datastore(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    course = models.CharField(max_length=100, null=False, blank=False)
    price= models.PositiveBigIntegerField(blank=False , null=False , default=0)
    email = models.EmailField(blank=False, null=False , help_text= "example12@gmail.com")
    number = models.PositiveBigIntegerField(blank=False , null=False, help_text="9700000000")
   



    class Meta:
        db_table = "students_info"
