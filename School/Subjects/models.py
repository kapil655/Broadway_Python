from django.db import models
from School.Teacher.models import Teacher

class Subject(models.Model):
    SUBJECT_TYPES = [
        ('theory', 'Theory'),
        ('practical', 'Practical'),
        ('lab', 'Lab'),
        ('elective', 'Elective'),
    ]
    
    # Basic Information
    subject_code = models.CharField(max_length=20, unique=True, blank=True)
    subject_name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=20, choices=SUBJECT_TYPES, default='theory')
    description = models.TextField(blank=True)
    
    # Teacher Assignment
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='subjects')
    
    # Class Information
    class_name = models.CharField(max_length=20) 
    
    # Academic Details
    credit_hours = models.IntegerField(default=1)
    full_marks = models.IntegerField(default=100)
    pass_marks = models.IntegerField(default=40)
    
    # Status
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Subjects"