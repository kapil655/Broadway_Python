from rest_framework import generics
from ..models import Teacher
from .serializer import TeacherSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer


class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'


class TeacherUpdateView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'


class TeacherDeleteView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'