from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from admin_dashboard.models import Book
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json

from comment.models import Comment

# Create your views here.


def index(request):
    
    data = Book.objects.all()
    
        
    
    
  #  return render(request,'json/home.html',{ 'data' : data } )
    da = serializers.serialize("json", data)
     #print(da)
    return HttpResponse(da)


def books(request):
    data = []
    books = Book.objects.all()
    
    for i in books:
       

        datas ={
            "book_title": i.book_title,
             "book_dec": i.book_description,
        "book_icon": "http://"+request.get_host()+i.book_image.url,
        "book_id": i.id,


        }
        data.append(datas)

          
    return HttpResponse(json.dumps(data))



def showslider(request):
    
    data = []
    books = Book.objects.all()
    
    for i in books:
       

        datas ={
            "book_title": i.book_title,
             "book_dec": i.book_description,
        "book_icon": "http://"+request.get_host()+i.book_image.url,
        "book_id": i.id

        }
        data.append(datas)

    
    
          
    return HttpResponse(json.dumps(data))
  #  for book in books:
     # books[book].



def book_comment(request,id):

    comments = Comment.objects.filter(postid=id).all()
    
    data = []

    for i in comments:

        datas = {
            "plople_name": i.name,
            "plople_comment": i.comment,
        }
        data.append(datas)
    
        
        
    return HttpResponse(json.dumps(data))






     
   