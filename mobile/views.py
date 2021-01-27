from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from admin_dashboard.models import Book
from admin_dashboard.models import Category
from comment.models import Comment
from django.contrib.postgres.search import SearchVector

# Create your views here.


def content(request,url):
    book = Book.objects.filter(book_url=url).first()
    meta = {
        "icon" : book.book_image,
        "title": book.book_title,
        "description": book.book_description,
        "keywords": book.keyboard,
        "pageUrl": request.get_full_path(),

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
    if "hide" in request.GET :
        dat = ""


        cat = Category.objects.filter(id=book.book_catid)
        data = Book.objects.filter(book_catid=cat[0].id)[:10]
        comments = Comment.objects.filter(postid=book.id)



        dat = {

                "book_image": book.book_image,
                "book_title": book.book_title,
                "book_description": book.book_description,
                "data": data,
                "cat": cat,
                "id": book.id,
                "comments" : comments,
                "schema" : True,
        }
        return render(request, "mobile/dashboard/load/content.html", dat)







    else:
        data = Book.objects.all()
        book = Book.objects.filter(book_url=url)
        catgory = Category.objects.all()
        ua = request.META.get('HTTP_USER_AGENT', '').lower()
        if ua.find("android") > 0:
            return render(request, 'mobile/dashboard/home.html', {'data': data, "cat": catgory,"meta" : meta})
        elif ua.find("iphone") > 0:
            return render(request, 'mobile/dashboard/home.html', {'data': data, "cat": catgory,"meta" : meta})
        else:
            return HttpResponseRedirect("http://"+request.get_host()+"/content/"+book[0].book_url+"/")






def showdatapdf(request,id):
    dat = ""
    book  = Book.objects.filter(id=id)
   # print(id)
    for da in book:
        dat = {
            "des":da.book_data
        }

    return render(request,"mobile/dashboard/load/onlinedata.html",dat)


def mobilecard(request,id):
    books = Book.objects.filter(book_catid=id).order_by('-id')[:10]

    return render(request,"mobile/dashboard/load/cardlist.html",{"book":books})
def home(request):
    data = Book.objects.all()
    catgory = Category.objects.all()
    return render(request,"mobile/dashboard/home.html",{'data': data,"cat": catgory})
def loadhome():
    return



def loadcontent():
    return None


def search(request):
    if request.method in "GET" and "search" in request.GET:
        search = request.GET["search"]
        book = Book.objects.annotate(search=SearchVector('book_title','keyboard', 'book_description'),).filter(search=search)
        cat = Category.objects.filter(cat_title=search)
        data = {
            "cat": cat,
            "book": book
        }
        return render(request, "mobile/dashboard/load/search.html", data)
    return HttpResponse("hello word")
def listview(request,cat):
    book = Book.objects.filter(book_catid=cat)
    ca = Category.objects.filter(id=cat)
    data = {
        "book" : book,
        "cat" : ca,
    }
    return  render(request,"mobile/dashboard/load/listview.html",data)

