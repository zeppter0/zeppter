from django.shortcuts import render

# Create your views here.
from admin_dashboard.models import Book
from django.http import HttpResponse
from django.utils import timezone


def dashboard(request):



        return render(request,'admin/dashboard.html')


def post(request):
    if request.method == 'POST' and 'title' in request.POST and  'description' in request.POST:
        title = request.POST['title']
        description = request.POST['description']

        if Book.objects.filter(book_title=title).count() <1:
            book = Book(book_title=title, book_description=description,
                        book_rates=2, book_publish=False, pub_date=timezone.now(), book_image="media/photo/img",
                        book_commit_id=1)
            book.save()
            return HttpResponse("save")
        else:
            return HttpResponse('allready')



    return HttpResponse('not found')