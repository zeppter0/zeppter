from django.shortcuts import render
from django.http import HttpResponse
from admin_dashboard.models import Book
import json
from comment.models import Comment


import math

# Create your views here.

def dashboard(request):
    data = Book.objects.all()
   # comments = Comment.objects.filter(postid=)
   #return HttpResponse("hello word")
    return render(request,'dashboard/main.html',{'data': data})
    #return HttpResponse("hello word")
def cardpost(request):
    data = Book.objects.all()
    st = list()


    for d in data:
        f = {"id": d.id,"img": d.book_image,"title" : d.book_title }
        st.append({"id":d.id,"title" : d.book_title,"des" : d.book_description,"img" : d.book_image.url})



    json_string = json.dumps(st)
   # print(json_string)


    return HttpResponse(json_string)

def view(request):
    return render(request,"./view.html")


def shows():
    return HttpResponse("dashboard")

def content(request,id):
    dat = "";

    data = Book.objects.filter(id=id)
    comments = Comment.objects.filter(postid=id)
    for d in data:
        d.book_data = d.book_data.replace("%*#h2","<h2>")
        d.book_data = d.book_data.replace("%*&h2","</h2>")
        dat = {'book_data' : d.book_data ,'title': d.book_title,'dascription':d.book_description,'img':d.book_image,'postid':id,'comments':comments}





    return render(request,"dashboard/content.html",dat)
def bookdata(request,id):
    data = Book.objects.filter(id=id)
    if data.count() == 1:
        book_data = data[0].book_data.replace("%*#h2", "<h2>")
        book_data = data[0].book_data.replace("%*&h2", "</h2>")
        return HttpResponse(book_data)

    return HttpResponse("hello word")


