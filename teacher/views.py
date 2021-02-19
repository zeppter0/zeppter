from django.shortcuts import render,HttpResponse
from teacher.middleware.middleware import Teather_login
from django.utils import decorators
from django.utils.decorators import method_decorator


from myuser.models import MyUeers
# Create your views here.

from django.views import View
from django.views.generic.base import TemplateView
@method_decorator(Teather_login,name="dispatch")
class Dashboard(View):
    def get(self,request):
        return render(request,"teacher/dashboard/home.html")





    def post(self,request):

        return


@method_decorator(Teather_login,name="dispatch")
class Children(View):
    def post(self,requst):
        children = MyUeers.objects()


