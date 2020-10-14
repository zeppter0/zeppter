from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from values import strings

def index(request,id):

    data = {
        "link" : strings.bootstrap
    }



    
    return render(request,"plopleadmin/home.html",data)
