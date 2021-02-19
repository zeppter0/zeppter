from django.db import models

# Create your models here.



class Subject(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="subject",default="404.jpg")





class School(models.Model):
    name = models.CharField(max_length=100)





class Photo(models.Model):
      name = models.CharField(max_length=50)
      photo =models.ImageField(upload_to="school/photo")
      updated_at = models.DateTimeField(auto_now=True)
