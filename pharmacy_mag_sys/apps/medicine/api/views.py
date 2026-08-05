from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.medicine.api.serializer import MedicineSerializer
from apps.medicine.models import Medicine


class MedicineView(GenericAPIView):
    queryset = Medicine
    serializer_class = MedicineSerializer


    def get(self, request, *args, **kwargs):
        data = Medicine.objects.all()
        serializer = MedicineSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MedicineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Medicine Created Successfully"
            })
        else:
            return Response(serializer.errors)