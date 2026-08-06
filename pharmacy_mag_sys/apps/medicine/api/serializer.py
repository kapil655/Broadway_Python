from rest_framework import serializers

from apps.medicine.models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        exclude = ['purchase_price']


    def to_representation(self, instance):

        data = super().to_representation(instance)

        if instance.category:
            print(instance.category.name)
            data['category_name'] = instance.category.name
        else:
            data['category_name'] = None

        return data