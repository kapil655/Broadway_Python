from rest_framework import serializers

from apps.pharmacy.models import Pharmacy

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'  

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.district:
            data['district_name'] = instance.district.name
        else:
            data['district_name'] = None

        return data
        