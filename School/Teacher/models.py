from django.db import models

# Create your models here.
class Teacher(models.Model):
    """Teacher model for school management system"""
    
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("on_leave", "On Leave"),
        ("terminated", "Terminated"),
    ]
    
    QUALIFICATION_CHOICES = [
        ("phd", "PhD"),
        ("masters", "Master's Degree"),
        ("bachelors", "Bachelor's Degree"),
        ("diploma", "Diploma"),
        ("certificate", "Certificate"),
    ]

    # Personal Data
    teacher_id = models.CharField(max_length=20, unique=True, blank=True, verbose_name="Teacher ID")
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES, blank=True, verbose_name="Qualification")
    specialization = models.CharField(max_length=100, blank=True, verbose_name="Specialization")
    experience_years = models.IntegerField(default=0, verbose_name="Years of Experience")
    joining_date = models.DateField(auto_now_add=True, verbose_name="Joining Date")

    class Meta:
        db_table = "Teacher"
        