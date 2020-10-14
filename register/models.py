from django.db import models

# Create your models here.


class  Rregister(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    school_name = models.CharField(max_length=500)
    gender = models.CharField(max_length=6)
    datetime = models.DateTimeField(auto_now=True)
    birth= models.DateTimeField()
    adhaar_card = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    email = models.CharField(max_length=50)





