import re

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
from myuser.models import MyUeers


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
    for d in book:

        print(re.sub(' +',' ',d.book_title.rstrip().lstrip().replace('\n', ' ').replace('\r', '')))
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


def bookdata(request,title):
    if "fdhjtgfhfc hjgkiujgkjgug jm,khkjhkj" == title:
        return HttpResponse("hello")




    return HttpResponse(title)

def shodata(request,title):
    dat = "";
    book = Book.objects.filter(book_title=title).first()
    cat = Category.objects.filter()
    meta = {
        "icon": book.book_image,
        "title": book.book_title,
        "description": book.book_description,
        "keywords": book.keyboard,
        "pageUrl": request.get_full_path(),
        "publishtime" : book.created_at,

        "auther": "devan mandal",
        "facebook": {
            "pageTitle": book.book_title,
            "description": book.book_description,
            "pageUrl": request.get_full_path(),
            "siteTitle": "zeppter",
            "homepageUrl": request.get_host(),

        },
        "google": {
            "pageTitle": book.book_title,
            "description": book.book_description,
            "pageUrl": request.get_full_path(),
            "homepageUrl": "zeppter",
        },
        "twitter": {
            "pageTitle": book.book_title,
            "description": book.book_description,
            "pageUrl": request.get_full_path(),
            "name": "zeppter",
        }
    }


    data = Book.objects.filter(id=book.id)[:5]
    comments = Comment.objects.filter(postid=book.id)
    for d in data:
        userd = MyUeers.objects.filter(id=d.publisher)
        user ={}
        if userd.count() ==1:

          user = {
              "fullname" : userd[0].first_name+" "+userd[0].last_name,
              "id" : userd[0].id
          }




        cat = Category.objects.filter(id=d.book_catid)
        d.book_data = d.book_data.replace("%*#h2", "<h2>")
        d.book_data = d.book_data.replace("%*&h2", "</h2>")
        dat = {'book_data': d.book_data,"user" : user ,"cat_title":cat[0].cat_title,"catid":d.book_catid, 'title': d.book_title, 'dascription': d.book_description,
               'img': d.book_image, 'postid': id, 'comments': comments ,'meta': meta,"schema": True}
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("android") > 0:
        return HttpResponseRedirect("http://" + request.get_host() + "/mobile/content/" + title)
    elif ua.find("iphone") > 0:
        return HttpResponseRedirect("http://" + request.get_host() + "/mobile/content/" + title)

    return render(request, "dashboard/showdata.html", dat)

def pdf_show(request,title):
    dat = "";
    data = Book.objects.filter(book_title=title).first()
    comments = Comment.objects.filter(postid=data.id)
    d = data


    dat = {'book_data': d.book_data,"link":bootstrap(), 'title': d.book_title, 'dascription': d.book_description,
               'img': d.book_image, 'postid': data.id, 'comments': comments,"pdf": d.data_book}
    return render(request,"dashboard/show_book.html",dat)



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