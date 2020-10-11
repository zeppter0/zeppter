from django.shortcuts import render

from django.http import HttpResponse
import cv2

def data(request):


    
    return render(request,"package/videocall.html")
    


def uploaddata(request):
    

    if(request.method == "GET"):
        return HttpResponse("hello word")
    elif(request.method == "POST"):
        photo_name = request.FILES["photo"]
       # file = open(request.FILES["photo"])


        return HttpResponse(photo_name.read())
    else:
        return HttpResponse("no data")
    
   

    

# Create your views here.
