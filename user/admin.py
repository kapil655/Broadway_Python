from django.contrib import admin
from user.models import UserBalance

# Register your models here.
@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']