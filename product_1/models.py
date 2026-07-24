from django.db import models


class School(models.Model):
    name = models.CharField(max_length=50, verbose_name="School Name")
    address = models.CharField(max_length=50, verbose_name="School Address")
    contact_number = models.CharField(max_length=15, verbose_name="Phone Number")
    school_mail = models.EmailField(verbose_name="School Email")

    def __str__(self):
        return f"{self.name} --> {self.address}"

    class Meta:
        db_table = "schools_info"


class Faculty(models.Model):
    school = models.ForeignKey(
        School,on_delete=models.RESTRICT,verbose_name="School",related_name="faculties")
    sub_name = models.CharField(max_length=50, verbose_name="Subject Name")
    school_open = models.TimeField()
    school_close = models.TimeField()

    def __str__(self):
        return f"{self.school.name} --> {self.sub_name}"

    class Meta:
        db_table = "faculty_info"


class Teacher(models.Model):
    school = models.ForeignKey(School,on_delete=models.RESTRICT,verbose_name="School",related_name="School_teachers"
    )
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=50, verbose_name="Address")
    number = models.CharField(max_length=15, verbose_name="Phone Number")

    def __str__(self):
        return f"{self.school.name} --> {self.number}"

    class Meta:
        db_table = "teacher_info"


class Grade(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="Teacher",related_name="grades"
    )
    grade = models.PositiveSmallIntegerField()
    no_of_subjects = models.ForeignKey(Faculty , on_delete=models.SET_NULL , verbose_name="Subjects", related_name="Teacher_subject")
  

    def __str__(self):
        return f"Grade {self.grade}"


class Student(models.Model):
    school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True, blank=True,related_name="students"
    )
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,related_name="students")
    name = models.CharField(max_length=100, verbose_name="Student Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "student_info"