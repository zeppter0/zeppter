from django.db import models

# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    email= models.EmailField()
    comment = models.CharField(max_length=500)