from django.shortcuts import render,redirect

# Create your views here.
from admin_dashboard.models import Book
from django.http import HttpResponse
from django.utils import timezone
from admin_dashboard.BookForm import BookUploadForm
from values.strings import bootstrap
from .models import Category



def dashboard(request):
    if request.user.is_authenticated:
<<<<<<< HEAD
        cat = Category.objects.all()

        data= {
            'link' : bootstrap(),
            'cat' : cat,
        }
        return render(request, 'admin/post.html',data)

    else:

        return  HttpResponse("please login")
=======
        return  HttpResponse("login home")
        
    else:
        return render(request,'admin/post.html')
        
>>>>>>> 0e5b86762ff9440cd555fb38d0cf73a356f399ac


def post(request):
    if request.method == 'POST' and 'title' in request.POST and 'description' in request.POST and 'book_add_pic' in request.FILES and 'book_data' in request.POST :
        title = request.POST['title']
        book = request.POST['book_data']
        description = request.POST['description']
        book_pic = request.FILES['book_add_pic']
        if Book.objects.filter(book_title=title).count() <1:
            book = Book(book_title=title, book_description=description,
                        book_data= book,
                        book_rates=2, book_publish=False, pub_date=timezone.now(), book_image=book_pic,
                        book_commit_id=1)
            book.save()
            return HttpResponse("save")
        else:
            return HttpResponse('allready')



    return redirect(dashboard)


def shows(request):
    data = Book.objects.all()
    return render(request,'admin/dashboard.html',{'data': data})


def addcategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['title'] != "":
                title = request.POST['title']
                file = request.FILES['file']
                cate = Category(cat_title=title, cat_img=file, cat_pub_date=timezone.now())
                if cate.save():
                    return HttpResponse("category seccesful")

                return HttpResponse("category not seccesful")


    return HttpResponse("category not seccesful")


