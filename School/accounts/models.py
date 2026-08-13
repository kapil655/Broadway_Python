from django.db import models

    # Create your models here.
class User(models.Model):
        ROLE_CHOICES = [
            ("admin","Admin"),
            ("teacher","Teacher"),
            ("student","Student"),
            ("staff","Staff"),
        ]
        Gender_Choice = [
            ("m","Male"),
            ("F","Female"),
            ("O","Other"),
        ]

        role = models.CharField(max_length=20 , choices=ROLE_CHOICES , default="Student")
        name = models.CharField(max_length=50, verbose_name="name")
        phone_number = models.CharField(max_length=15, blank=True, null=True)
        address = models.TextField(blank=True, null=True)
        date_of_birth = models.DateField(null=True, blank=True)
        gender = models.CharField(max_length=1, choices=Gender_Choice, blank=True)
        is_verified = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            db_table="accounts"
            
