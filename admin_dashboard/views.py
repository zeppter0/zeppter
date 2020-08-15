from django.shortcuts import render

# Create your views here.
from admin_dashboard.models import Book
from django.http import HttpResponse
from django.utils import timezone
from admin_dashboard.BookForm import BookUploadForm



def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin/dashboard.html')
    else:
        return  HttpResponse("please login")


def post(request):
    if request.method == 'POST' and 'title' in request.POST and  'description' in request.POST and 'book_add_pic' in request.FILES:
        title = request.POST['title']
        description = request.POST['description']
        book_pic = request.FILES['book_add_pic']
        if Book.objects.filter(book_title=title).count() <1:
            book = Book(book_title=title, book_description=description,
                        book_rates=2, book_publish=False, pub_date=timezone.now(), book_image=book_pic,
                        book_commit_id=1)
            book.save()
            return HttpResponse("save")
        else:
            return HttpResponse('allready')



    return HttpResponse('not found')


