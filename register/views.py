from django.shortcuts import render
from values import strings
# Create your views here.
def register(request):
    data = {
        "link": strings.bootstrap,
    }
    return render(request,"login/register.html",data)
