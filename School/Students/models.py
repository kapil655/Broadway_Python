from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    
    CLASS_CHOICES = [
        ("1", "Class 1"),
        ("2", "Class 2"),
        ("3", "Class 3"),
        ("4", "Class 4"),
        ("5", "Class 5"),
        ("6", "Class 6"),
        ("7", "Class 7"),
        ("8", "Class 8"),
        ("9", "Class 9"),
        ("10", "Class 10"),
        ("11", "Class 11"),
        ("12", "Class 12"),
    ]
    
    SECTION_CHOICES = [
        ("A", "Section A"),
        ("B", "Section B"),
        ("C", "Section C"),
    ]
    
    # Personal Information
    student_id = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Academic Information
    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES, blank=True)
    roll_number = models.IntegerField(default=0)
    admission_date = models.DateField(auto_now_add=True)
    
    # Contact Information
    address = models.TextField(blank=True)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField(blank=True, null=True)
    
    # Status and Metadata
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    absent = models.BooleanField(default=False)


    class Meta:
        db_table="students"
