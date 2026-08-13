from rest_framework import generics
from ..models import Subject
from .serializer import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all().order_by('-id')
    serializer_class = SubjectSerializer


class SubjectCreateView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'id'


class SubjectUpdateView(generics.UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'id'


class SubjectDeleteView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'id'