from django.shortcuts import render ,HttpResponse

# Create your views here.

from django.utils.decorators import method_decorator

from students.middleware.authstudent import Student_login


from myuser.models import MyUeers, Teacher, Student
# Create your views here.

from django.views import View
from django.views.generic.base import TemplateView

from teacher.models import Work


@method_decorator(Student_login,name="dispatch")
class Dashboard(View):
    def get(self,reguest):
        return render(reguest,"students/dashboard/home.html")


    def post(self,request):
        return render(request,"students/dashboard/load/show.html")


@method_decorator(Student_login,name="dispatch")
class taxtnow(View):


    def post(self,requst):
      #  id = MyUeers.objects.get(email=requst.session["email"],student=True)

        #teacher = MyUeers.objects.get(pk=requst.POST.get("id"))
        text = Work.objects.get(user_id=int(requst.POST.get("id"))).task

        return HttpResponse(text,content_type='application/liquid')



