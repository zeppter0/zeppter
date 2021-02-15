import json

from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from admin_dashboard.models import Book, Views, Like, DisLike
from admin_dashboard.models import Category
from comment.models import Comment
from django.contrib.postgres.search import SearchVector

# Create your views here.
from myuser.models import MyUeers
from django.contrib.auth.hashers import make_password, check_password

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
        view = Views.objects.filter(post_id=[book.id])
        likes = Like.objects.filter(post_id=book.id).count()
        dislike = DisLike.objects.filter(post_id=book.id).count()


        dat = {
            "views": view.count(),
            "likes" : likes,
            "dislikes" : dislike,


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
        user_data = {}
        if "email" in request.session:
            emai = request.session["email"]

            user_data = MyUeers.objects.get(email=emai)
        data = Book.objects.all()
        book = Book.objects.filter(book_url=url)
        catgory = Category.objects.all()
        ua = request.META.get('HTTP_USER_AGENT', '').lower()
        if ua.find("android") > 0:
            return render(request, 'mobile/dashboard/home.html', {"userdata" : user_data,'data': data, "cat": catgory,"meta" : meta})
        elif ua.find("iphone") > 0:
            return render(request, 'mobile/dashboard/home.html', {"userdata" : user_data,'data': data, "cat": catgory,"meta" : meta})
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
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("android") > 0:
        if request.method in "GET" and "hide" in request.GET:
            if "show" == request.GET["hide"]:
                book = Book.objects.filter(book_arrcat=[cat])
                ca = Category.objects.filter(id=cat)
                data = {
                    "book": book,
                    "cat": ca,
                }
                return render(request, "mobile/dashboard/load/listview.html", data)

        return render(request, "mobile/dashboard/home.html", )




    elif ua.find("iphone") > 0:
        if request.method in "GET" and "hide" in request.GET:
            if "show" == request.GET["hide"]:
                book = Book.objects.filter(book_arrcat=[cat])
                ca = Category.objects.filter(id=cat)
                data = {
                    "book": book,
                    "cat": ca,
                }
                return render(request, "mobile/dashboard/load/listview.html", data)

        return render(request, "mobile/dashboard/home.html", )
    else:
        return  HttpResponseRedirect("/catlist/"+str(cat))





def sitemap(request):


    book = Book.objects.all()
    return render(request,'mobile/include/sitemap.xml',{"books":book}, content_type="application/xhtml+xml")


def login(request):
    check = "nodata"


    email = ""
    if "email" in request.session:
        emails = request.session['email']
        myuser = MyUeers.objects.filter(email=emails).first()
        if myuser.email == emails:
            email = myuser.email
            check = "deshboard"
        return HttpResponse(json.dumps({"email":email,"check":check}))



    elif request.method in "POST" and "email" in request.POST and "password" in request.POST:
        email_q = request.POST['email']
        password = request.POST['password']
        myuser = MyUeers.objects.filter(email=email_q)

        if myuser.count() == 1:
            checkd = check_password(password, myuser[0].password)
            if checkd :
                ud = request.session["email"] = myuser[0].email
                email = myuser[0].email
                check = "deshboard"
            else:
                 check = "password"

        else:
            check  = "email"
        return HttpResponse(json.dumps({"email": email, "check": check}))











    return render(request,"mobile/login/load/login.html")





def register(request):
    checklogin = "nodata"
    if 'email' in request.session:
        checklogin =  "login"

    elif request.method in "POST" and 'email' \
            in request.POST and 'first_name' \
            in request.POST and 'last_name' \
            in request.POST and 'mobile_no' \
            in request.POST and 'gender' \
            in request.POST and "password1" \
            in request.POST and "password2":

        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_no = request.POST['mobile_no']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        pass4 = make_password(password1)
        if password1 == password2:
            myuser = MyUeers.objects.filter(email=email)
            if myuser.count() < 1:
                user = MyUeers(gender=gender, first_name=first_name,
                               last_name=last_name, email=email, password=pass4, mobile_no=int(mobile_no))
                user.save()
                request.session['email'] = email
                checklogin ="register"
            else:
                checklogin = "user"
        else:
            checklogin = "password"
        return HttpResponse(json.dumps({"check":checklogin}))

    else:


        return render(request,"mobile/login/load/register.html")


def userprofile(request,id):
    user = MyUeers.objects.get(pk=id)

    return render(request,"mobile/admin/user_profile.html",{"user": user ,"userdata" :user})