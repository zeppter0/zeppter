import os

from urllib import request
from urllib.error import HTTPError, URLError

from django.core.files import File
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
from django.urls import reverse
from django.core.validators import int_list_validator


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

    book_arrcat = ArrayField(models.IntegerField(),default=[1])
    book_arrcatstr = models.CharField(max_length=40,default="1")
    keyboard = models.CharField(max_length=5000 ,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publisher = models.IntegerField()
    book_url = models.CharField(max_length=300)


    def delete(self, using=None, keep_parents=False):
        self.book_image.storage.delete(self.book_image.name)
        self.data_book.storage.delete(self.data_book.name)
        super().delete()


    def __str__(self):
        return self.book_title

    def get_remote_image(self,image_url):
        if image_url and not self.book_image:
            try:
                result = request.urlretrieve(image_url)
                self.book_image.save(
                    os.path.basename(image_url),
                    File(open(result[0], 'rb'))
                )
                self.save()
            except HTTPError as e:
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            except URLError as e:
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            else:
                print('Website is working fine')






    def get_absolute_url(self):
        return "/content/"+str(self.book_url)






class Category(models.Model):
    id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=50)
  #  book_category = models.CharField(max_length=50,default="empty")
    cat_img = models.ImageField(upload_to='cat_img',default=None)
    cat_pub_date = models.DateTimeField(auto_now_add=True)
    def delete(self, using=None, keep_parents=False):
        self.cat_img.storage.delete(self.cat_img.name)

        super().delete()

class ImgUpload(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.IntegerField()
    title = models.CharField(max_length=500)
    img_pub_date = models.DateTimeField("date published")
    img = models.ImageField(upload_to='cat_img/content',default='')




