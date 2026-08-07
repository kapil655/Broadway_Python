from django.urls import path
from apps.medicine.api.views import CategoryView, MedicineView,UpdateMedicineView

urlpatterns = [
    path('',MedicineView.as_view()),
    path('cats',CategoryView.as_view()),
]