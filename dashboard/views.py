from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template.response import TemplateResponse

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
    data = Book.objects.all().order_by('-id')[:3]
    carousel = "hhh"
    catgory= Category.objects.all()
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    meta = {
        "title" : "zeppter book story and status hindi offers",
        "description" : "zeppter hindi,love, kids, horror story top most story love status ",
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
        return render(request, 'dashboard/main.html', {'data': data,"meta" : meta,"cat" : catgory,"carousel" : carousel})
    else:
        return render(request, 'dashboard/main.html', {'data': data ,"meta" : meta , "cat" : catgory })








    #return HttpResponse("hello word")
def cardpost(request,catid):
    book = Book.objects.filter(book_catid=catid).order_by('-id')[:10]
    st = list()






    return render(request,"dashboard/cardlist.html",{"book" : book})

def view(request):
    return render(request,"./view.html")


def shows():
    return HttpResponse("dashboard")

def content(request,id):
    book = Book.objects.filter(id=id)
    meta = {
        "icon": book[0].book_image,
        "title": book[0].book_title,
        "description": book[0].book_description,
        "keywords": book[0].keyboard,
        "pageUrl": request.get_full_path(),

        "auther": "devan mandal",
        "facebook": {
            "pageTitle": book[0].book_title,
            "description": book[0].book_description,
            "pageUrl": request.get_full_path(),
            "siteTitle": "zeppter",
            "homepageUrl": request.get_host(),

        },
        "google": {
            "pageTitle": book[0].book_title,
            "description": book[0].book_description,
            "pageUrl": request.get_full_path(),
            "homepageUrl": "zeppter",
        },
        "twitter": {
            "pageTitle": book[0].book_title,
            "description": book[0].book_description,
            "pageUrl": request.get_full_path(),
            "name": "zeppter",
        }
    }
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("linux") >0:
        dat = "";

        data = Book.objects.filter(id=id)[:5]
        comments = Comment.objects.filter(postid=id)
        for d in data:
            d.book_data = d.book_data.replace("%*#h2", "<h2>")
            d.book_data = d.book_data.replace("%*&h2", "</h2>")
            dat = {'book_data': d.book_data, 'title': d.book_title, 'dascription': d.book_description,
                   'img': d.book_image, 'postid': id, 'comments': comments}

        return render(request, "dashboard/content.html", {"meta" : meta})


def bookdata(request,id):
    data = Book.objects.filter(id=id)
    if data.count() == 1:
        book_data = data[0].book_data.replace("%*#h2", "<h2>")
        book_data = data[0].book_data.replace("%*&h2", "</h2>")
        return HttpResponse(book_data)

    return HttpResponse("hello word")

def shodata(request,id,title):
    dat = "";
    book = Book.objects.filter(id=id)
    cat = Category.objects.filter()
    meta = {
        "icon": book[0].book_image,
        "title": book[0].book_title,
        "description": book[0].book_description,
        "keywords": book[0].keyboard,
        "pageUrl": request.get_full_path(),
        "publishtime" : book[0].created_at,

        "auther": "devan mandal",
        "facebook": {
            "pageTitle": book[0].book_title,
            "description": book[0].book_description,
            "pageUrl": request.get_full_path(),
            "siteTitle": "zeppter",
            "homepageUrl": request.get_host(),

        },
        "google": {
            "pageTitle": book[0].book_title,
            "description": book[0].book_description,
            "pageUrl": request.get_full_path(),
            "homepageUrl": "zeppter",
        },
        "twitter": {
            "pageTitle": book[0].book_title,
            "description": book[0].book_description,
            "pageUrl": request.get_full_path(),
            "name": "zeppter",
        }
    }

    data = Book.objects.filter(id=id)[:5]
    comments = Comment.objects.filter(postid=id)
    for d in data:
        d.book_data = d.book_data.replace("%*#h2", "<h2>")
        d.book_data = d.book_data.replace("%*&h2", "</h2>")
        dat = {'book_data': d.book_data, 'title': d.book_title, 'dascription': d.book_description,
               'img': d.book_image, 'postid': id, 'comments': comments ,'meta': meta,"schema": True}
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("linux")>0:
        return render(request, "dashboard/showdata.html",dat)


    elif ua.find("window")>0:
        return render(request, "dashboard/showdata.html")
    else:
        return HttpResponseRedirect("http://"+request.get_host()+"/mobile/content/"+"/"+str(id))

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


def sitema(request):
    book = Book.objects.all()

    return render(request,"include/sitemap.xml",{"book":book})


def robots(request):
    return render(request, "include/robot.txt")