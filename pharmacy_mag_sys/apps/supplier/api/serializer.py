from rest_framework import serializers  # type: ignore[import]

from apps.supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'