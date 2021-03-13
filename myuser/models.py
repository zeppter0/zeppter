from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from teacher.models import Subject,School

# Create your models here.
class MyUeers(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='user',default="404_user.png")

   # username = models.CharField(max_length=50)
    email  =  models.EmailField(max_length=50)
    password = models.CharField(max_length=200)
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    mobile_no = models.BigIntegerField(default=1)


    def __str__(self):
        return self.email



class Teacher(models.Model):
    user = models.IntegerField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    school = models.ForeignKey(School,models.CASCADE)


    students = ArrayField(models.IntegerField())




class Student(models.Model):
    user = models.IntegerField()
    class_id = models.CharField(max_length=20)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    teachers = ArrayField(models.IntegerField())



