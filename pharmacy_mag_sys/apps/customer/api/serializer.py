from rest_framework import serializers
from apps.customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.category:
            data['category_name'] = instance.category.name
            return data