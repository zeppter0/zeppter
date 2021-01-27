import os

from urllib import request

from django.core.files import File
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
from django.urls import reverse


class Book(models.Model):
    id = models.AutoField(primary_key=True)

    book_title = models.CharField(max_length=5000,default=None)
    book_description = models.CharField(max_length=1000,default=None)
    book_image = models.ImageField(upload_to='cat_img',default='')
    book_rates = models.IntegerField(default=5)
    book_commit_id = models.IntegerField()
    book_data = models.CharField(max_length=100000,default="")
    book_upload_date = models.DateTimeField("date published")
    book_publish = models.BooleanField(default=False)
    data_book = models.FileField("zip_data",default=None)
    book_catid = models.IntegerField(default=1)
    book_arrcat = ArrayField(ArrayField(models.IntegerField()))
    keyboard = models.CharField(max_length=5000 ,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publisher = models.IntegerField()
    book_url = models.CharField(max_length=100)

    def delete(self, using=None, keep_parents=False):
        self.book_image.storage.delete(self.book_image.name)
        self.data_book.storage.delete(self.data_book.name)
        super().delete()


    def __str__(self):
        return self.book_title

    def get_remote_image(self,image_url):
        if image_url and not self.book_image:
            result = request.urlretrieve(image_url)
            self.book_image.save(
                os.path.basename(image_url),
                File(open(result[0], 'rb'))
            )
            self.save()

    def get_absolute_url(self):
        return "/content/"+str(self.book_title)






class Category(models.Model):
    id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=50)
  #  book_category = models.CharField(max_length=50,default="empty")
    cat_img = models.ImageField(upload_to='cat_img',default=None)
    cat_pub_date = models.DateTimeField("date published")
    def delete(self, using=None, keep_parents=False):
        self.cat_img.storage.delete(self.cat_img.name)

        super().delete()

class ImgUpload(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.IntegerField()
    title = models.CharField(max_length=500)
    img_pub_date = models.DateTimeField("date published")
    img = models.ImageField(upload_to='cat_img/content',default='')




