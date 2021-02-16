from datetime import datetime

from django.db import models
from myuser.models import MyUeers
# Create your models here.



class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.CharField(max_length=30)
    contentid = models.IntegerField()
    userid = models.IntegerField()
    comment = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date_published', auto_now=True)



