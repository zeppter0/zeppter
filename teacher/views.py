from django.shortcuts import render,HttpResponse
from teacher.middleware.middleware import Teather_login
from django.utils import decorators
from django.utils.decorators import method_decorator


from myuser.models import MyUeers
# Create your views here.

from django.views import View
from django.views.generic.base import TemplateView

from teacher.models import Work


@method_decorator(Teather_login,name="dispatch")
class Dashboard(View):
    def get(self,request):

        return render(request,"teacher/dashboard/home.html")





    def post(self,request):
        children = MyUeers.objects.filter(student=True)

        return render(request,"teacher/dashboard/load/children.html",{"students":children})




@method_decorator(Teather_login,name="dispatch")
class Children(View):
    def post(self,requst):


        return HttpResponse("hllo word")



@method_decorator(Teather_login,name="dispatch")
class Works(View):
    def get(self,request):
        return render(request,"teacher/dashboard/load/worklist.html")
    def post(self,request):
        text = request.POST.get("text")

        return render(request,"teacher/dashboard/load/works.html")

@method_decorator(Teather_login,name="dispatch")
class worktext(View):
    def post(self,request):


        user = MyUeers.objects.get(email=request.session.get("email"))
        work = Work.objects.filter(user_id=user.pk)
        if work.count() <1:
            wk =  Work(user_id=user.pk,task=request.POST.get("text"))
            wk.save()

        elif work.count() == 1:
            work.update(task=request.POST.get("text"))


        return HttpResponse(("sesses"))




