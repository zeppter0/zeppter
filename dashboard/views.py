from django.shortcuts import render
from django.http import HttpResponse
from admin_dashboard.models import Book

# Create your views here.

def dashboard(request):
    b = Book(book_title='kese ho')


    return HttpResponse(b.book_description)
