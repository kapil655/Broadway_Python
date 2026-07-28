from django.db import models

# Create your models here.


class Project(models.Model):
        name = models.CharField(max_length=100, help_text="enter your project full name")
        email = models.EmailField()
        start_date = models.DateField()
        end_date = models.DateField(null=True, blank=True)
        is_active = models.BooleanField(blank=False,default=True)
        
       
       

        def __str__(self):
             return f" {self.name} ->{self.start_date}"

      
        
        class Meta:
            db_table="Projects"
            