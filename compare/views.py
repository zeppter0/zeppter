from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView



class Homw(View):
    def get(self,request):
        return render(request,"compare/home.html")

class Product(TemplateView):
    template_name = 'compare/main_content.html'