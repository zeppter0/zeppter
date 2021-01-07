
from django.http import HttpResponse
from django.shortcuts import render
class content:

    def down(request):



        return render(request,"dashboard/showdata.html")