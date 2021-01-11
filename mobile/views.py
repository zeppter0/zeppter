from django.shortcuts import render
from django.http import HttpResponse
from admin_dashboard.models import Book
from admin_dashboard.models import Category
from comment.models import Comment
from django.contrib.postgres.search import SearchVector

# Create your views here.


def content(request,id):
    if "hide" in request.GET :
        dat = ""
        book = Book.objects.filter(id=id)

        cat = Category.objects.filter(id=book[0].book_catid)
        data = Book.objects.filter(book_catid=cat[0].id)[:10]
        comments = Comment.objects.filter(postid=id)

        print(cat)
        for da in book:
            dat = {
                "book_image": da.book_image,
                "book_title": da.book_title,
                "book_description": da.book_description,
                "data": data,
                "cat": cat,
                "id": da.id,
                "comments" : comments,
            }

        return render(request, "mobile/dashboard/load/content.html", dat)


    else:
        data = Book.objects.all()
        catgory = Category.objects.all()
        return render(request, 'mobile/dashboard/home.html', {'data': data, "cat": catgory})




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
        book = Book.objects.annotate(search=SearchVector('book_title', 'book_description'),).filter(search=search)
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

