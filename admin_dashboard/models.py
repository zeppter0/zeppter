from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)

    book_title = models.CharField(max_length=50,default=None)
    book_description = models.CharField(max_length=500,default=None)
    book_image = models.ImageField(upload_to='cat_img',default='')
    book_rates = models.IntegerField(default=5)
    book_commit_id = models.IntegerField()
    book_data = models.CharField(max_length=100000)
    book_upload_date = models.DateTimeField("date published")
    book_publish = models.BooleanField(default=False)



    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.book_title


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=50)
  #  book_category = models.CharField(max_length=50,default="empty")
    cat_img = models.ImageField(upload_to='cat_img',default=None)
    cat_pub_date = models.DateTimeField('date published')

