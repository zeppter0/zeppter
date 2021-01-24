from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import NameForm


# Create your views here.


def imageupload(request):
    if request.method in "POST":

        return HttpResponse()



  
    return render(request,"test/cemera.html")
