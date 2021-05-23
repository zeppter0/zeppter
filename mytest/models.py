from django.db import models

# Create your models here.


class Reddit(models.Model):
    name = models.CharField(max_length=10)
    position = models.IntegerField()