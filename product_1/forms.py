from django import forms
from django.core.exceptions import ValidationError
from .models import Student, Teacher, Attendance, School, Faculty, Grade
from datetime import date

# ==================== STUDENT FORM ====================
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and (age < 5 or age > 18):
            raise ValidationError('Student age must be between 5 and 18')
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise ValidationError('Phone number must contain only digits')
        return phone


# ==================== TEACHER FORM ====================
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'address', 'number', 'school', 'faculty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and (age < 18 or age > 65):
            raise ValidationError('Teacher age must be between 18 and 65')
        return age

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if number and not number.isdigit():
            raise ValidationError('Phone number must contain only digits')
        return number


# ==================== ATTENDANCE FORM ====================
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'present', 'absent', 'date']  # Changed to match your model
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'absent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default date to today
        if not self.instance.pk:
            self.fields['date'].initial = date.today()

    def clean(self):
        cleaned_data = super().clean()
        present = cleaned_data.get('present')
        absent = cleaned_data.get('absent')
        
        # Ensure both present and absent are not True at the same time
        if present and absent:
            raise ValidationError('Student cannot be both present and absent')
        
        # Ensure at least one is selected
        if not present and not absent:
            raise ValidationError('Please select either Present or Absent')
        
        attendance_date = cleaned_data.get('date')
        if attendance_date and attendance_date > date.today():
            raise ValidationError('Attendance cannot be marked for future dates')
        return cleaned_data


# ==================== SCHOOL FORM ====================
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address', 'cl_number', 'cl_mail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'cl_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'cl_mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }


# ==================== FACULTY FORM ====================
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['school', 'sub_name', 'school_open', 'school_close']
        widgets = {
            'school': forms.Select(attrs={'class': 'form-control'}),
            'sub_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject name'}),
            'school_open': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'school_close': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }


# ==================== GRADE FORM ====================
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['teacher', 'grade', 'subject']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter grade number'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade and (grade < 1 or grade > 12):
            raise ValidationError('Grade must be between 1 and 12')
        return grade