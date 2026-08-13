from rest_framework import generics
from School.accounts.models import User
from .serializers import AttendanceSerializer


class AttendanceListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AttendanceSerializer