from django.shortcuts import render
from django.http import HttpResponse
from admin_dashboard.models import Book

# Create your views here.

def dashboard(request):
    data = Book.objects.all();


    return render(request,'dashboard/main.html',{'data': data})
