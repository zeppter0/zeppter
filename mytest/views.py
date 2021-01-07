from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import NameForm


# Create your views here.


def imageupload(request):
    #hello
    if request.POST == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
  
    return render(request,"test/cemera.html",{"form" : form})
