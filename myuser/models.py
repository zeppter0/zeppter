from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

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
    mobile_no = models.BigIntegerField(default=1)
    def __str__(self):
        return self.email




