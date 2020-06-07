from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField

    book_title = models.CharField(max_length=50,default=None)
    book_description = models.CharField(max_length=500,default=None)
    book_image = models.ImageField(upload_to='book_img',default='')
    book_rates = models.IntegerField(default=5)
    book_commit_id = models.IntegerField()
    book_publish = models.BooleanField(default=False)



    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.book_title




