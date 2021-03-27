import json

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View

from admin_dashboard.models import Book, Views, Like, DisLike
from admin_dashboard.models import Category
from comment.models import Comment
from django.contrib.postgres.search import SearchVector

# Create your views here.
from myuser.models import MyUeers
from django.contrib.auth.hashers import make_password, check_password

from zeppter import settings


def content(request,url):
    user_data = {}
    if "email" in request.session:
        emai = request.session["email"]

        user_data = MyUeers.objects.get(email=emai)
    book = Book.objects.filter(book_url=url).first()
    img =  ""
    img = book.book_image
    meta = {
        "icon" : img,
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
        comments = Comment.objects.filter(contentid=book.id)
        view = Views.objects.filter(post_id=[book.id])
        likes = Like.objects.filter(post_id=book.id).count()
        dislike = DisLike.objects.filter(post_id=book.id).count()

        comme = []

        for d in comments:
             user_g = MyUeers.objects.get(pk=d.userid)
             comme.append({"id" : d.pk ,"userid" : user_g.pk,"photo": user_g.photo ,"comment" : d.comment,"user_name":user_g.first_name+" "+user_g.last_name} )


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
                "comments" : comme,
                "schema" : True,
            "userdata": user_data,
        }

        return render(request, "mobile/dashboard/load/content.html", dat)







    else:

        data = Book.objects.all()
        book = Book.objects.filter(book_url=url)
        catgory = Category.objects.all()
        ua = request.META.get('HTTP_USER_AGENT', '').lower()
        if ua.find("android") > 0:
            return render(request, 'mobile/dashboard/home.html', {"userdata" : user_data,'data': data, "cat": catgory,"meta" : meta})
        elif ua.find("iphone") > 0:
            return render(request, 'mobile/dashboard/home.html', {"userdata" : user_data,'data': data, "cat": catgory,"meta" : meta})
        else:
            return HttpResponseRedirect(request.scheme+"://"+request.get_host()+"/content/"+book[0].book_url+"/")






def showdatapdf(request,id):
    dat = ""
    book  = Book.objects.filter(id=id)
   # print(id)
    for da in book:
        dat = {
            "des":da.book_data,
            "title" : da.book_title,
            "img" : da.book_image
        }

    return render(request,"mobile/dashboard/load/onlinedata.html",dat)


def mobilecard(request,id):
    books = Book.objects.filter(book_arrcat__overlap=[id]).order_by('-id')[:10]

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
        searc = request.GET["search"]
        from translate import Translator
        translator = Translator(to_lang="hi")  # initalize the Translator object
        search = translator.translate(searc )  # translate two phrases to Hindi
        book = Book.objects.annotate(search=SearchVector('keyboard','book_title'),).filter(search=search)
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

            if "show" == request.GET["hide"] :



                book = Book.objects.filter(book_arrcat__overlap=[cat])
                paginator = Paginator(book, 10)



                page = request.GET.get('page')

                profile = paginator.get_page(page)

                ca = Category.objects.filter(id=cat)
                data = {
                    "book": profile,
                    "cat": ca,
                    'catid' : ca.first().pk
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
                return HttpResponse(json.dumps({"check":checklogin,"user": user.first_name}))


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

class Donations(View):
    def get(self,request):
        return render(request,'donations/mobile.html')