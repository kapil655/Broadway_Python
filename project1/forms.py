from django import forms
from project1.models import datastore

class DatastoreForm(forms.ModelForm):
    class Meta:
        model = datastore
        fields = '__all__'