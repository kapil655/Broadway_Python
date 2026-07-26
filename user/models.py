from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_balance")
    balance = models.PositiveIntegerField()

    def __str__(self):
        return  f'{self.user.username} - {self.balance}'

    class Meta:
        db_table = "user_balance"


class UserImage(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="userimage")


    def __str__(self):
        return  f'{self.name}'

    class Meta:
        db_table = "user_image"