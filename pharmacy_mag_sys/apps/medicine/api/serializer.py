from rest_framework import serializers

from apps.medicine.models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        exclude = ['purchase_price']


    def to_representation(self, instance):

        data = super().to_representation(instance)

        if instance.category:
            data['category_name'] = instance.category.name
            return data
        