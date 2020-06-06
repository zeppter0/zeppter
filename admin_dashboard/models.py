from django.db import models

# Create your models here.
class Book(models.Model):

    book_title = models.CharField(max_length=50,default=None)
    book_description = models.CharField(max_length=500,default=None)
    book_image = models.CharField(max_length=500)
    book_rates = models.IntegerField(default=5)
    book_commit_id = models.IntegerField()
    book_publish = models.BooleanField(default=False)


    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.book_title




