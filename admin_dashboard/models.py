import os
"""    if image_url and not self.book_image:
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
                print('Website is working fine') """
from urllib import request
from urllib.error import HTTPError, URLError

from django.core.files import File
from django.db import models
from django.contrib.postgres.fields import ArrayField
import requests
from django.core import files
import tempfile

# Create your models here.
from django.urls import reverse
from django.core.validators import int_list_validator


class Tag(models.Model):
    word        = models.CharField(max_length=35)
    slug        = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.word

class Book(models.Model):
    id = models.AutoField(primary_key=True)

    book_title = models.CharField(max_length=100000,default=None)
    book_description = models.CharField(max_length=100000,default=None)
    book_image =  ArrayField(models.CharField(max_length=1000,default=""))
    book_rates = models.IntegerField(default=5)
    book_commit_id = models.IntegerField()
    book_data = models.CharField(max_length=100000,default="")
    book_upload_date = models.DateTimeField("date published")
    book_publish = models.BooleanField(default=False)

    book_catid = models.IntegerField(default=1)

    book_arrcat = ArrayField(models.IntegerField(),default=[1])
    book_arrcatstr = models.CharField(max_length=40,default="1")
    keyboard = models.CharField(max_length=100000 ,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publisher = models.IntegerField()
    book_url = models.CharField(max_length=300)
    specifications = models.CharField(default="",max_length=1000000)
    brand = models.CharField(default="",max_length=100)
    model = models.CharField(default="",max_length=1000)
   # tags = models.ManyToManyField(Tag)








    def delete(self,*args,**kwargs):
        if os.path.isfile(self.book_image.path):
            os.remove(self.book_image.path)

        super(Book, self).delete(*args, **kwargs)


    def __str__(self):
        return self.book_title+" "+str(self.id)

    def get_remote_image(self,image_url):
        

    


            image_save =  requests.get(image_url,stream=True)
            if image_save.ok:
                
                file_name = image_url.split('/')[-1]
                lf = tempfile.NamedTemporaryFile()
                for block in image_save.iter_content(1024 * 8):
        
                     # If no more file then stop
                     if not block:
                        break

                     lf.write(block)
                self.book_image.save(file_name,files.File(lf))
                self.save()     


               



                # self.book_image.save(
                 #   os.path.basename(image_url),
                #    File(open(image_save.text, 'rb'))
                # )
                # self.save()
             #   print(os.path.basename(image_url))



            # self.book_image.save(
            #   os.path.basename(image_url),
            #    File(open(image_save.text, 'rb'))
            # )
            # self.save()
        #   print(os.path.basename(image_url))

    def get_absolute_url(self):
        return "/content/"+str(self.book_url)









class Category(models.Model):
    id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=500)
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




class Shops(models.Model):
    id = models.AutoField(primary_key=True)
    book_id  = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(default="" ,max_length=1000)
    shipping = models.CharField(default="",max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)







