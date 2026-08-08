# apps/pharmacy/api/serializers.py
from rest_framework import serializers
from apps.pharmacy.models import Pharmacy, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_id', 'name']


class PharmacySerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district.name', read_only=True)
    
    class Meta:
        model = Pharmacy
        fields = [
            'id', 'name', 'registration_number', 'email', 'phone', 
            'website', 'address', 'city', 'district', 'district_name',
            'opening_time', 'closing_time', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']