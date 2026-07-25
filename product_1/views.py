from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils import timezone
from .models import Teacher, Student, Attendance, Grade, School
from .forms import StudentForm, AttendanceForm, TeacherForm, SchoolForm

def home(request):
    """Dashboard home page"""
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_schools': School.objects.count(),
        'recent_attendance': Attendance.objects.select_related('student').order_by('-date')[:10],
        'today_attendance': Attendance.objects.filter(date=timezone.now().date()).count(),
        'grades_with_students': Grade.objects.annotate(student_count=Count('students')),
    }
    return render(request, "projects/home.html", context)


# ==================== SCHOOL VIEWS ====================

def view_schools(request):
    """List all schools"""
    schools = School.objects.all().annotate(
        teacher_count=Count('teachers'),
        student_count=Count('students')
    )
    return render(request, 'projects/schools.html', {
        'schools': schools
    })

def school_detail(request, school_id):
    """View school details with teachers and students"""
    school = get_object_or_404(School, id=school_id)
    teachers = school.teachers.all().select_related('faculty')
    students = school.students.all().select_related('grade')
    faculties = school.faculties.all()
    
    context = {
        'school': school,
        'teachers': teachers,
        'students': students,
        'faculties': faculties,
        'teacher_count': teachers.count(),
        'student_count': students.count(),
        'faculty_count': faculties.count(),
    }
    return render(request, 'projects/school_detail.html', context)

def add_school(request):
    """Add new school"""
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'School added successfully!')
            return redirect('view_schools')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SchoolForm()
    
    return render(request, 'projects/add_school.html', {
        'form': form
    })

def edit_school(request, school_id):
    """Edit school details"""
    school = get_object_or_404(School, id=school_id)
    
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, 'School updated successfully!')
            return redirect('school_detail', school_id=school.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SchoolForm(instance=school)
    
    return render(request, 'projects/edit_school.html', {
        'form': form,
        'school': school
    })

def delete_school(request, school_id):
    """Delete school"""
    school = get_object_or_404(School, id=school_id)
    
    if request.method == 'POST':
        school_name = school.name
        school.delete()
        messages.success(request, f'School "{school_name}" deleted successfully!')
        return redirect('view_schools')
    
    return render(request, 'projects/delete_school.html', {
        'school': school
    })


# ==================== TEACHER VIEWS ====================

def view_teachers(request):
    """List all teachers"""
    teachers = list(Teacher.objects.select_related('school', 'faculty').all())
    return render(request, 'projects/teachers.html', {
        'teachers': teachers
    })

def teacher_detail(request, teacher_id):
    """View teacher details"""
    teacher = get_object_or_404(Teacher, id=teacher_id)
    grades = teacher.grades.all()
    students = Student.objects.filter(grade__in=grades)
    return render(request, 'projects/teacher_detail.html', {
        'teacher': teacher,
        'grades': grades,
        'students': students
    })

def add_teacher(request):
    """Add new teacher"""
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher added successfully!')
            return redirect('view_teachers')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TeacherForm()
    
    return render(request, 'projects/add_teacher.html', {
        'form': form
    })

def edit_teacher(request, teacher_id):
    """Edit teacher details"""
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher updated successfully!')
            return redirect('teacher_detail', teacher_id=teacher.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TeacherForm(instance=teacher)
    
    return render(request, 'projects/edit_teacher.html', {
        'form': form,
        'teacher': teacher
    })

def delete_teacher(request, teacher_id):
    """Delete teacher"""
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        teacher_name = teacher.name
        teacher.delete()
        messages.success(request, f'Teacher "{teacher_name}" deleted successfully!')
        return redirect('view_teachers')
    
    return render(request, 'projects/delete_teacher.html', {
        'teacher': teacher
    })


# ==================== STUDENT VIEWS ====================

def view_students(request):
    """List all students"""
    students = Student.objects.select_related('school', 'grade').all()
    return render(request, 'projects/students.html', {
        'students': students
    })

def student_detail(request, student_id):
    """View student details"""
    student = get_object_or_404(Student, id=student_id)
    attendance = student.attendance.all().order_by('-date')
    return render(request, 'projects/student_detail.html', {
        'student': student,
        'attendance': attendance
    })

def add_student(request):
    """Add new student"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('view_students')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    return render(request, 'projects/add_student.html', {'form': form})


# ==================== ATTENDANCE VIEWS ====================

def mark_attendance(request):
    """Mark attendance for students"""
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance marked successfully!')
            return redirect('mark_attendance')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AttendanceForm()
    
    today = timezone.now().date()
    today_attendance = Attendance.objects.filter(date=today)
    students = Student.objects.all()
    
    return render(request, 'projects/mark_attendance.html', {
        'form': form,
        'today_attendance': today_attendance,
        'students': students
    })

def attendance_report(request):
    """Generate attendance report"""
    date_filter = request.GET.get('date')
    status_filter = request.GET.get('status')
    
    attendance = Attendance.objects.select_related('student')
    
    if date_filter:
        attendance = attendance.filter(date=date_filter)
    
    # Filter by status (present or absent)
    if status_filter == 'present':
        attendance = attendance.filter(present=True)
    elif status_filter == 'absent':
        attendance = attendance.filter(absent=True)
    
    return render(request, 'projects/attendance_report.html', {
        'attendance': attendance,
        'date_filter': date_filter,
        'status_filter': status_filter
    })


# ==================== API / AJAX VIEWS ====================

def search_students(request):
    """AJAX search for students"""
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET.get('q')
        students = Student.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        ).values('id', 'name', 'grade__grade')
        return JsonResponse(list(students), safe=False)
    return JsonResponse([], safe=False)