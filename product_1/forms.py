from django import forms
from django.core.exceptions import ValidationError
from .models import Student, Teacher, Attendance, School, Faculty, Grade, Subject
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
        fields = ['name', 'age', 'address', 'number', 'school', 'faculty', 'subjects']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 150px;'}),
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


# ==================== SUBJECT FORM ====================
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'level', 'description', 'credit_hours', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject code (e.g., MATH101)'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'credit_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter credit hours'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# ==================== GRADE FORM ====================
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['teacher', 'grade', 'subject', 'subjects']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 150px;'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        teacher = cleaned_data.get('teacher')
        grade = cleaned_data.get('grade')
        
        if teacher and grade:
            if Grade.objects.filter(teacher=teacher, grade=grade).exists():
                if self.instance.pk:
                    if Grade.objects.filter(teacher=teacher, grade=grade).exclude(pk=self.instance.pk).exists():
                        raise ValidationError('This grade already exists for this teacher')
                else:
                    raise ValidationError('This grade already exists for this teacher')
        return cleaned_data


# ==================== ATTENDANCE FORM ====================
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'present', 'absent', 'date']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'absent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['date'].initial = date.today()

    def clean(self):
        cleaned_data = super().clean()
        present = cleaned_data.get('present')
        absent = cleaned_data.get('absent')
        
        if present and absent:
            raise ValidationError('Student cannot be both present and absent')
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