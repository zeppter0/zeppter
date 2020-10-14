from django.shortcuts import render
from admin_dashboard.models import Book
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


def index(request):
    
     data = Book.objects.all()
    
        
    
    
  #  return render(request,'json/home.html',{ 'data' : data } )
     da = serializers.serialize("json", data)
     print(da)
     return HttpResponse(da)
   