from django.shortcuts import render,redirect

# Create your views here.
from admin_dashboard.models import Book
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
from admin_dashboard.BookForm import BookUploadForm
from values.strings import bootstrap
from .models import Category
from admin_dashboard.models import ImgUpload
import json




def dashboard(request):
    if request.user.is_authenticated:

        cat = Category.objects.all()

        data= {
            'link' : bootstrap(),
            'cat' : cat,
        }
        return render(request, 'admin/post.html',data)

    else:

        cat = Category.objects.all()

        data= {
            'link' : bootstrap(),
            'cat' : cat,
        }
        return render(request, 'admin/post.html',data)



def post(request):

    if request.method == 'POST' and 'title' in request.POST and 'description' in request.POST and 'book_add_pic' in request.FILES and 'pdf_show' in request.FILES and 'editor1' in request.POST :


        title = request.POST['title']

        book = request.POST['editor1']
        description = request.POST['description']
        book_pic = request.FILES['book_add_pic']
        book_pdf = request.FILES['pdf_show']
        book_publish = request.POST['publish']
        book_catid = request.POST["cat"]
        keyboard = request.POST["keyboard"]
        book_cat = request.POST["cateid"]
        cat_json = json.loads(book_catid)
        print(book)


        if Book.objects.filter(book_title=title).count() < 1 :
            book = Book(book_title=title,
                        book_description=description,
                        data_book=book_pdf,
                        book_data=book,
                        book_arrcat=cat_json,
                        book_rates=2,
                        keyboard=keyboard,
                        book_publish=False,
                        book_upload_date=timezone.now(),
                        book_image=book_pic,
                        book_catid=int(book_cat),
                        book_commit_id=1)
            book.save()
            json_post = {
                "id": book.id,
                "cat" : cat_json,

                "response": "post is secucessful publish"
            }
            return HttpResponse(json.dumps(json_post))
        else:
            return HttpResponse('allready')



    return HttpResponse("please data check")


def shows(request):
    data = Book.objects.all()
    return render(request,'admin/dashboard.html',{'data': data})


def addcategory(request):


        if request.method == "POST":
            if request.POST['title'] != "":
                title = request.POST['title']
                file = request.FILES['file']
                cate = Category(cat_title=title, cat_img=file, cat_pub_date=timezone.now())
                if cate.save():
                    return HttpResponse("category seccesful")

                return HttpResponse("category not seccesful hello"+request.POST['title']  )




def post_delele(request,id):
   pa = ""
   da = Book.objects.filter(id=id).delete()




   return HttpResponse(pa)
def cat_delete(request,id):
    Category.objects.filter(id=id).delete()
    return HttpResponse("catgory is deleted")
def imgupload(request,id):
    global img
    if request.method == "POST" and "title" in request.POST and "img" in request.FILES:
        title = request.POST["title"]
        contfile = request.FILES["img"]
        img = ImgUpload(postid=id,title=title,img=contfile )
        img.save()





    return HttpResponse("http://"+request.get_host()+"cat_img/content"+img[0].img)


def post_update(request):
    if request.method == 'POST' and 'title' in request.POST and 'description' in request.POST and 'book_add_pic' in request.FILES and 'pdf_show' in request.FILES and 'book_data' in request.POST and "id" in request.POST:


        title = request.POST['title']
        book = request.POST['book_data']
        description = request.POST['description']
        book_pic = request.FILES['book_add_pic']
        book_pdf = request.FILES['pdf_show']
        book_publish = request.POST['publish']
        book_id = request.POST['id']

        if book_publish == "true":
            book = Book.objects.filter(id=int(book_id)).update(book_title=title, book_description=description,
                        data_book=book_pdf,
                        book_data=book,
                        book_rates=2, book_publish=False, book_upload_date=timezone.now(), book_image=book_pic,
                        book_commit_id=1)

            json_post = {

                "response": "post is secucessful publish"
            }
            return HttpResponse(book_id)
        else:
            return HttpResponse(book_publish)
    else:
        return HttpResponse("no data")
    return HttpResponse("please data check")


def googled9d554441dd811fd(request):
    return HttpResponse()