from django.db import models


class School(models.Model):
    name = models.CharField(max_length=50, verbose_name="School Name")
    address = models.CharField(max_length=100, verbose_name="School Address")
    cl_number = models.CharField(max_length=20, verbose_name="Phone Number")
    cl_mail = models.EmailField(max_length=50, verbose_name="School Email")

    def __str__(self):
        return f"{self.name} --> {self.address}"

    class Meta:
        db_table = "schools_info"


class Faculty(models.Model):
    school = models.ForeignKey(School,on_delete=models.RESTRICT,verbose_name="School",related_name="faculties")
    sub_name = models.CharField(max_length=50, verbose_name="Subject Name")
    school_open = models.TimeField()
    school_close = models.TimeField()

    def __str__(self):
        return f"{self.school.name} --> {self.sub_name}"

    class Meta:
        db_table = "faculty_info"


class Teacher(models.Model):
    school = models.ForeignKey(School,on_delete=models.RESTRICT,verbose_name="School",related_name="teachers")
    faculty = models.ForeignKey(Faculty,on_delete=models.RESTRICT,verbose_name="Faculty",related_name="teachers")
    name = models.CharField(max_length=30,verbose_name="Teacher Name")
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=50,verbose_name="Address")
    number = models.CharField(max_length=15,verbose_name="Phone Number")

    def __str__(self):
        return f"{self.name} --> {self.faculty.sub_name}"

    class Meta:
        db_table = "teacher_info"


class Grade(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="Teacher", related_name="grades")
    grade = models.PositiveSmallIntegerField(
        verbose_name="Grade")
    subject = models.ForeignKey(Faculty,on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Subject", related_name="grades")
    def __str__(self):
        return f"Grade {self.grade}"


class Student(models.Model):
    school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="School",related_name="students")
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name="Grade",related_name="students")
    name = models.CharField(max_length=100,verbose_name="Student Name")
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=100,verbose_name="Address")
    phone = models.CharField(max_length=15,verbose_name="Phone Number",blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "student_info"


class Attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name="Student",related_name="attendance")

    present = models.BooleanField(
        default=False)

    absent = models.BooleanField(
        default=False)

    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} --> {self.date}"

    class Meta:
        db_table = "attendance_info"