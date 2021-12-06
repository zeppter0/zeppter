from django.shortcuts import render
from django.http import FileResponse
from zeppter.settings import BASE_DIR
from django.views import View

# Create your views here.
class Img(View):


    def get(self,request,url):
       return FileResponse(open(BASE_DIR+"/file/img/"+url, 'rb'))




