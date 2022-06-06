from django.db import models
# Create your models here.
class Student(models.Model):
    gender_choice=(
        ('M','Male'),
        ('F','Female'),
    )
    year = (
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE')
    )
    prog = (
        ('BIT', 'Bachelor of Science in Information Technology'),
        ('BAC', 'Bachelor of Accountancy'),
        ('BAIT', 'Bachelor of Accountancy in Information Technology'),
        ('BBF', 'Bachelor of Banking and Finance'),
        ('BCS', 'Bachelor of Computer Science'),
        ('BEF', 'Bachelor of Economics and Finance')
    )
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    student_id=models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=gender_choice)
    programme = models.CharField(max_length=50,choices=prog)
    year=models.CharField(max_length=8,choices=year)
    pic=models.ImageField(upload_to ='profilepics')
    def __str__(self):
        return self.student_id

class Staff(models.Model):
    gender_choice=(
        ('M','Male'),
        ('F','Female'),
    )
    department_choice = (
        ('DCISM','Department of Computing,Information systems and Mathematics'),
        ('DBAF','Department of Banking, Finance and Economics'),
        ('DA','Department of Accountancy')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    staff_id=models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices = gender_choice)
    department = models.CharField(max_length=50,choices=department_choice)
    pic=models.ImageField(upload_to ='profilepics')
    def __str__(self):
        return self.staff_id

class Visitor(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=40,null=True)
    visitor_id=models.CharField(max_length=100)
    contact=models.CharField(max_length=100,null=True)
    reason=models.CharField(max_length=100,null=True)
    go_to = models.CharField(max_length=100,null=True)
    anchor_id = models.CharField(max_length=100,null=True)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.visitor_id

