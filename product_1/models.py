from django.db import models
from django.core.exceptions import ValidationError

class School(models.Model):
    name = models.CharField(max_length=50, verbose_name="School Name")
    address = models.CharField(max_length=100, verbose_name="School Address")
    cl_number = models.CharField(max_length=20, verbose_name="Phone Number")
    cl_mail = models.EmailField(max_length=50, verbose_name="School Email")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "schools_info"
        ordering = ['name']


class Faculty(models.Model):
    school = models.ForeignKey(School, on_delete=models.RESTRICT, verbose_name="School", related_name="faculties")
    sub_name = models.CharField(max_length=50, verbose_name="Subject Name")
    school_open = models.TimeField()
    school_close = models.TimeField()

    def __str__(self):
        return f"{self.school.name} --> {self.sub_name}"

    class Meta:
        db_table = "faculty_info"
        ordering = ['sub_name']
        verbose_name_plural = "Faculties"


class Subject(models.Model):
    """Subject model with all educational levels"""
    LEVEL_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11 (+2)'),
        ('12', 'Grade 12 (+2)'),
        ('bachelor', 'Bachelors'),
        ('master', 'Masters'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Subject Name")
    code = models.CharField(max_length=20, verbose_name="Subject Code", unique=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Level")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    credit_hours = models.PositiveSmallIntegerField(default=3, verbose_name="Credit Hours")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

    class Meta:
        db_table = "subjects_info"
        ordering = ['level', 'name']
        verbose_name_plural = "Subjects"
        unique_together = ['name', 'level']


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.RESTRICT, verbose_name="School", related_name="teachers")
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, verbose_name="Faculty", related_name="teachers")
    name = models.CharField(max_length=30, verbose_name="Teacher Name")
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=50, verbose_name="Address")
    number = models.CharField(max_length=15, verbose_name="Phone Number")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="teachers", verbose_name="Subjects")
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.age < 18 or self.age > 65:
            raise ValidationError({'age': 'Age must be between 18 and 65'})

    class Meta:
        db_table = "teacher_info"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['school']),
        ]


class Grade(models.Model):
    LEVEL_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11 (+2)'),
        ('12', 'Grade 12 (+2)'),
        ('bachelor', 'Bachelors'),
        ('master', 'Masters'),
    ]
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Teacher", related_name="grades")
    grade = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Grade")
    subject = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Subject", related_name="grades")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="grades", verbose_name="Subjects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_grade_display()} - {self.teacher.name}"

    class Meta:
        ordering = ['grade']
        unique_together = ['grade', 'teacher']


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="School", related_name="students")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="Grade", related_name="students")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=100, verbose_name="Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number", blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.age < 5 or self.age > 18:
            raise ValidationError({'age': 'Student age must be between 5 and 18'})

    class Meta:
        db_table = "student_info"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['grade']),
        ]


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student", related_name="attendance")
    present = models.BooleanField(default=False)
    absent = models.BooleanField(default=False)
    date = models.DateField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student.name} --> {self.date} ({status})"

    def clean(self):
        if self.present and self.absent:
            raise ValidationError('Student cannot be both present and absent')
        if not self.present and not self.absent:
            raise ValidationError('Please select either Present or Absent')

    class Meta:
        db_table = "attendance_info"
        ordering = ['-date']
        unique_together = ['student', 'date']
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['student', 'date']),
        ]