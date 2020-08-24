from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField('emp_name',max_length=50)
    age= models.IntegerField('emp_age')
    salary = models.FloatField('emp_salary')
    desig = models.CharField('emp_designation',max_length=50)


class Student(models.Model):
    name = models.CharField('stud_name', max_length=50)
    age = models.IntegerField('stud_age')
    fees = models.FloatField('stud_fees')
    course = models.CharField('stud_course', max_length=50)
