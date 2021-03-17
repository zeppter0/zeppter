import re

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template.response import TemplateResponse

from admin_dashboard.models import Book, Views, Like, DisLike
import json

from dashboard.Pakage import ArrayAppend
from dashboard.showdata import content
from values.strings import bootstrap
from admin_dashboard.models import Category
from django.template.loader import render_to_string


from comment.models import Comment
from myuser.models import MyUeers


import math
from django.contrib.postgres.search import SearchVector
import goslate

# Create your views here.

def dashboard(request):
    user_data = ""
    if "email" in request.session:
        email = request.session["email"]
        user_data = MyUeers.objects.filter(email=email).first()
        print("user name ")

    data = Book.objects.all().order_by('-id')[:3]
    carousel = "hhh"
    catgory= Category.objects.all()[:3]


    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    meta = {
        "title" : "zeppter book story and status hindi offers",
        "description": "zeppter book kahaniya khana banane ka tarika bollywood kahaniya love best story in hindi bangali story,most marvel hingh  ",
        "googlePlusId" : "zeppter0",
        "keywords" : "zeppter,hindi story,horror story,love story,kids story,bollywood story,hindi kahaniya,bangali story",
        "pageUrl" : request.get_full_path(),

        "auther"  : "devan mandal",
        "facebook" : {
            "pageTitle" : "zeppter hindi story kid",

            "imageUrl": "/static/assets/img/zeppter.png",
            "type" : "website",

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



        return render(request, 'mobile/dashboard/home.html', {'data': data,"userdata": user_data ,"meta" : meta ,"cat": catgory})


    elif ua.find("iphone")>0:
        return render(request, 'mobile/dashboard/home.html', {'data': data,"userdata": user_data, "meta": meta, "cat": catgory})
    elif ua.find("linux")>0:
        return render(request, 'dashboard/main.html', {'data': data,"userdata": user_data,"meta" : meta,"cat" : catgory,"carousel" : carousel,"website":True})
    else:
        return render(request, 'dashboard/main.html', {"userdata": user_data,'data': data ,"meta" : meta , "cat" : catgory ,"website":True})








    #return HttpResponse("hello word")
def cardpost(request,catid):
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    print("cat_id :"+str(catid))
    book = Book.objects.filter(book_arrcat__overlap=[catid]).order_by('-id')[:10]
    for d in book:

        print(re.sub(' +',' ',d.book_title.rstrip().lstrip().replace('\n', ' ').replace('\r', '')))
    st = list()

    if ua.find("linux")>0:
        return render(request, "dashboard/cardlist.html", {"book": book})

    else:
        return render(request, "dashboard/cardlist.html", {"book": book})









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
        dat = ""

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

def shodata(request,url):
    dat = ""
    user_data = ""
    if "email" in request.session:
        email = request.session["email"]
        user_data = MyUeers.objects.filter(email=email).first()
        print("user name ")
    book = Book.objects.filter(book_url=url).first()
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
            "imageUrl" : "/media/"+str(book.book_image),
            "type" :"book",
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
    comments = Comment.objects.filter(contentid=book.id)
    comme = []

    for d in comments:
        user_g = MyUeers.objects.get(pk=d.userid)
        comme.append({"id": d.pk, "userid": user_g.pk, "photo": user_g.photo, "comment": d.comment,

                      "date" : d.pub_date,"email":user_g.email,
                      "user_name": user_g.first_name + " " + user_g.last_name})

    for d in data:
        userd = MyUeers.objects.filter(id=d.publisher)
        user ={}

        if userd.count() ==1:
          views =  Views.objects.filter(ip_address=get_client_ip(request),post_id=[d.id])

          if views.count() <1:
              vi = Views(ip_address=get_client_ip(request),post_id=[d.id])
              vi.save()



          user = {
              "fullname" : userd[0].first_name+" "+userd[0].last_name,
              "id" : userd[0].id
          }
        dst = []
        for ca in d.book_arrcat:
            dst.append(Category.objects.filter(id=ca)[0])









        d.book_data = d.book_data.replace("%*#h2", "<h2>")
        d.book_data = d.book_data.replace("%*&h2", "</h2>")
        like = Like.objects.filter(post_id=d.id).count()
        dislike = DisLike.objects.filter(post_id=d.id).count()
        vie = Views.objects.filter(post_id=[d.id])
        dat = {"like":like,"userdata":user_data,"dislike":dislike,"views": vie.count(),"publish_date":d.created_at,"url" : d.book_url,'book_data': d.book_data,"user" : user ,"cats":dst, 'title': d.book_title, 'dascription': d.book_description,
               'img': d.book_image,"create_b": d.created_at,"update_b": d.updated_at, 'postid': d.id, 'comments': comme ,'meta': meta,"book": True}
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("android") > 0:
        return HttpResponseRedirect(request.scheme+"://" + request.get_host() + "/mobile/content/" + url+"/")
    elif ua.find("iphone") > 0:
        return HttpResponseRedirect(request.scheme+"://" + request.get_host() + "/mobile/content/" + url+"/")

    return render(request, "dashboard/showdata.html", dat)

def pdf_show(request,url):
    dat = ""
    data = Book.objects.filter(book_url=url).first()
    comments = Comment.objects.filter(postid=data.id)
    d = data

    user_data = ""
    if "email" in request.session:
        email = request.session["email"]
        user_data = MyUeers.objects.filter(email=email).first()
        print("user name ")




    dat = {"userdata":user_data,'book_data': d.book_data,"link":bootstrap(), 'title': d.book_title, 'dascription': d.book_description,
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

    data = Book.objects.all()[:3]
    catgory = Category.objects.all()[:3]
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


def contect(request):
    return render(request,"dashboard/contact.html")


def morelist(request):

    title = ""
    books= []
    if request.method == "GET":
        searc = request.GET['search']

        from googletrans import Translator

        translator = Translator()  # initalize the Translator object
        search = translator.translate(searc, dest='hi').text  # translate two phrases to Hindi
        print(search)
        books = Book.objects.annotate(
            search=SearchVector('book_title'),
        ).filter(search=search)
        bd = Book.objects.all()

        paginator = Paginator(books, 15)  # So limited to 5 profiles in a page

        page = request.GET.get('page')

        profile = paginator.get_page(page)  # data
        user_data ={}
        if 'email' in request.session:
            email = request.session['email']

            user_data = MyUeers.objects.get(email=email)
        return render(request, "dashboard/morelist.html", {"userdata":user_data,"title":search, 'profiles': profile})


def catlist(request,id):
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("android")>0:
        return HttpResponseRedirect("/mobile/listview/"+str(id)+"/")
    if ua.find("iphone")>0:
        return HttpResponseRedirect("/mobile/listview/" + str(id) + "/")

    books = Book.objects.filter(book_arrcat__overlap=[id])
    cat = Category.objects.filter(id=id).first().cat_title
    paginator = Paginator(books, 15)  # So limited to 5 profiles in a page


    page = request.GET.get('page')

    profile = paginator.get_page(page)  # data
    return render(request, "dashboard/morelist.html", {"title": cat, 'profiles': profile})


def about(request):
    meta = {




    }

    return render(request,"dashboard/about.html",{"logo":True})

PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )

def get_client_ip(request):
    """get the client ip from the request
    """
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip


def user_profile(request,id):





    data = MyUeers.objects.filter(id=id)
    if data.count() ==1:


        return render(request,'dashboard/user_profile.html',{"data": data.first(),"userdata": data.first()})



    return None