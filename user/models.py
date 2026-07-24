from django.db import models
from django.contrib.auth.models import User

class UserBalance(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_balance"
    )
    balance = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.user.username} ---> {self.balance}"

    class Meta:
        db_table = "User_Balance"

        