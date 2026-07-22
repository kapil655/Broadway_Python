from django.db import models

# Create your models here.
class School(models.Model):
    
    name = models.CharField(max_length=50, help_text="Enter school name", verbose_name="School Name")
    phone_number = models.PositiveBigIntegerField()
    address = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f'{self.name}-{self.phone_number}'
    class Meta:
        db_table = "school"




class Student(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE , verbose_name="school Name" , related_name="Student_School")
    name = models.CharField(max_length=50, verbose_name="Student Name")
    age = models.PositiveSmallIntegerField()
    dob = models.DateField()
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "student"

    


