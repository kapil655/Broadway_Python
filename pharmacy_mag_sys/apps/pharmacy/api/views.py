# apps/pharmacy/api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from apps.pharmacy.models import Pharmacy
from apps.pharmacy.api.serializers import PharmacySerializer


class PharmacyListView(generics.ListAPIView):
    """GET only - list all pharmacies"""
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PharmacyCreateView(generics.CreateAPIView):
    """POST only - create a new pharmacy"""
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [permissions.AllowAny]


class PharmacyUpdateView(generics.UpdateAPIView):
    """PUT/PATCH only - update a pharmacy"""
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class PharmacyDeleteView(generics.DestroyAPIView):
    """DELETE only - delete a pharmacy"""
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'