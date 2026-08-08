from django import forms
from apps.medicine.models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields='__all__'
      