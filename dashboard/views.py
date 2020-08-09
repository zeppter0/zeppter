from django.shortcuts import render
from django.http import HttpResponse
from admin_dashboard.models import Book
import json

# Create your views here.

def dashboard(request):
    data = Book.objects.all()


    return render(request,'dashboard/main.html',{'data': data})
def cardpost(request):
    data = Book.objects.all()
    st = list()


    for d in data:
        f = {"img": d.book_image,"title" : d.book_title }
        st.append({"title" : d.book_title,"des" : d.book_description,"img" : d.book_image.url})



    json_string = json.dumps(st)
   # print(json_string)


    return HttpResponse(json_string)
