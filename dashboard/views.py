from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from admin_dashboard.models import Book
import json
from dashboard.showdata import content
from values.strings import bootstrap
from admin_dashboard.models import Category
from django.template.loader import render_to_string


from comment.models import Comment


import math

# Create your views here.

def dashboard(request):
    data = Book.objects.all()[:5]
    catgory= Category.objects.all()
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    meta = {
        "title" : "zeppter hindi story kid ",
        "description" : "zeppter hindi story top big rock story",
        "keyboard" : "zeppter,hindi story,top story",
        "pageUrl" : request.get_full_path(),

        "auther"  : "devan mandal",
        "facebook" : {
            "pageTitle" : "zeppter hindi story kid",
            "description": "zeppter hindi story top big rock story",
            "pageUrl": request.get_full_path(),
            "siteTitle" : "zeppter",
            "homepageUrl" : request.get_host(),


        } ,
        "google" : {
            "pageTitle": "zeppter hindi story kid",
            "description": "zeppter hindi story top big rock story",
            "pageUrl": request.get_full_path(),
            "homepageUrl": "zeppter",
        },
        "twitter" : {
            "pageTitle": "zeppter hindi story kid",
            "description": "zeppter hindi story top big rock story",
            "pageUrl": request.get_full_path(),
            "name": "zeppter",
        }
    }
   # comments = Comment.objects.filter(postid=)
   #
    if ua.find("android")>0:



        return render(request, 'mobile/dashboard/home.html', {'data': data ,"meta" : meta ,"cat": catgory})


    elif ua.find("iphone")>0:
        return render(request, 'mobile/dashboard/home.html', {'data': data, "meta": meta, "cat": catgory})
    elif ua.find("linux")>0:
        return render(request, 'dashboard/main.html', {'data': data})
    else:
        return render(request, 'dashboard/main.html', {'data': data})








    #return HttpResponse("hello word")
def cardpost(request):
    data = Book.objects.filter(book_catid=1)[:10]
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
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("linux") >0:
        dat = "";

        data = Book.objects.filter(id=id)
        comments = Comment.objects.filter(postid=id)
        for d in data:
            d.book_data = d.book_data.replace("%*#h2", "<h2>")
            d.book_data = d.book_data.replace("%*&h2", "</h2>")
            dat = {'book_data': d.book_data, 'title': d.book_title, 'dascription': d.book_description,
                   'img': d.book_image, 'postid': id, 'comments': comments}

        return render(request, "dashboard/content.html", dat)


def bookdata(request,id):
    data = Book.objects.filter(id=id)
    if data.count() == 1:
        book_data = data[0].book_data.replace("%*#h2", "<h2>")
        book_data = data[0].book_data.replace("%*&h2", "</h2>")
        return HttpResponse(book_data)

    return HttpResponse("hello word")

def shodata(request,id):
    dat = "";

    data = Book.objects.filter(id=id)
    comments = Comment.objects.filter(postid=id)
    for d in data:
        d.book_data = d.book_data.replace("%*#h2", "<h2>")
        d.book_data = d.book_data.replace("%*&h2", "</h2>")
        dat = {'book_data': d.book_data, 'title': d.book_title, 'dascription': d.book_description,
               'img': d.book_image, 'postid': id, 'comments': comments}
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("linux")>0:
        return render(request, "dashboard/showdata.html",dat)


    elif ua.find("window")>0:
        return render(request, "dashboard/showdata.html")
    else:
        return HttpResponse(get_template('dashboard/igul.html'))

def pdf_show(request,id):
    dat = "";

    data = Book.objects.filter(id=id)
    comments = Comment.objects.filter(postid=id)
    for d in data:
        d.book_data = d.book_data.replace("%*#h2", "<h2>")
        d.book_data = d.book_data.replace("%*&h2", "</h2>")
        dat = {'book_data': d.book_data,"link":bootstrap(), 'title': d.book_title, 'dascription': d.book_description,
               'img': d.book_image, 'postid': id, 'comments': comments,"pdf": d.data_book}
    return render(request,"dashboard/PDF_show.html",dat)



def listview(request,id):
    post = Book.objects.all()
    list =3
    data = {
        "data" : post,
        "list": list
    }
    return render(request,"mobile/dashboard/listview.html",data)



def mobile_home(request):

    data = Book.objects.all()
    catgory = Category.objects.all()
#    rengred = render_to_string("mobile/dashboard/load/home.html",{"data":data,"cat":catgory})
  #  print(render(request,"mobile/dashboard/load/home.html",{"book":data,"data":data,"cat":catgory}))
    return render(request,"mobile/dashboard/load/home.html",{"book":data,"data":data,"cat":catgory})


def googled9d554441dd811fd(request):
    return HttpResponse("google-site-verification: googled9d554441dd811fd.html")