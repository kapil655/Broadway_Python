from django.db import models

# Create your models here.


class Pharmacy(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="Medical Name")
    registration_number = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField(verbose_name="Medical contact number", unique=True)
    website = models.URLField(blank=True)
    address = models.CharField(max_length=30, verbose_name="Medical address")
    city = models.CharField(max_length=10, choices=City.choices)
    district = models.CharField(max_length=10, choices=District.choices)
    country = models.CharField(max_length=10, choices=Country.choices)
    opening_time = models.DateField()
    closing_time = models.DateField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Pharmacy"

    def __str__(self):
        return self.name