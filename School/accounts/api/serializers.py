from rest_framework import serializers
from School.accounts.models import User


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'role', 'phone_number', 'date_of_birth', 'gender']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['full_name'] = instance.name
        return data