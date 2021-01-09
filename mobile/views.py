from django.shortcuts import render
from admin_dashboard.models import Book
from admin_dashboard.models import Category

# Create your views here.


def content(request,id):
    if "hide" in request.GET :
        dat = ""
        book = Book.objects.filter(id=id)

        cat = Category.objects.filter(id=book[0].book_catid)
        data = Book.objects.filter(book_catid=cat[0].id)

        print(cat)
        for da in book:
            dat = {
                "book_image": da.book_image,
                "book_title": da.book_title,
                "book_description": da.book_description,
                "data": data,
                "cat": cat,
                "id": da.id,
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
    books = Book.objects.filter(book_catid=id)

    return render(request,"mobile/dashboard/load/cardlist.html",{"book":books})
def home(request):
    data = Book.objects.all()
    catgory = Category.objects.all()
    return render(request,"mobile/dashboard/home.html",{'data': data,"cat": catgory})
def loadhome():
    return



def loadcontent():
    return None