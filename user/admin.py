from django.contrib import admin
from user.models import UserBalance, UserImage

# Register your models here.
@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user','balance']


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ['name']