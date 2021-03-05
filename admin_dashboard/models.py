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
    book_data = models.CharField(max_length=1000000,default="")
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



    def delete(self,*args,**kwargs):
        if os.path.isfile(self.book_image.path):
            os.remove(self.book_image.path)

        super(Book, self).delete(*args, **kwargs)


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
class Views(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField(null=True)
    post_id = ArrayField(models.IntegerField())
    updated_at = models.DateTimeField(auto_now=True)
class Like(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.CharField(max_length=60)
    post_id = models.IntegerField()
class DisLike(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=60)
    post_id = models.IntegerField()





