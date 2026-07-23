from django import forms
from .models import Grade, Student

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
