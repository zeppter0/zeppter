from django.contrib.auth import authenticate
from django.shortcuts import render ,redirect
from values import strings
from register.models import Rregister
from django.http import HttpResponse
from django.contrib.auth.models import User
import hashlib
# Create your views here.
def register(request):
    data = {
        "link": strings.bootstrap,
    }
    if(request.user.is_authenticated):
        return render(request, "login/register.html", data)
    else:
          return HttpResponse("hello word")



def upregister(request):

    if request.method == "POST" and request.POST["email"] !="" and request.POST["first_name"] != "" and request.POST["last_name"]\
            and request.POST["school_name"] != "" and request.POST["gender"] != "":
        check = Rregister.objects.filter(email=request.POST["email"]).count()



        if check == 0:
            modelinsertdata(request)
            if request.user.is_authenticated:
                return HttpResponse("hello word")

        else:
            return HttpResponse("user data allready")



    else:
        return HttpResponse("error data")



def modelinsertdata(request):
    first_name = request.POST["first_name"];
    last_name = request.POST["last_name"];
    School_name = request.POST["school_name"];
    gender = request.POST["gender"];
    address = request.POST["address"];
    birth = request.POST["yy"]+"-"+request.POST["mm"]+"-"+request.POST["dd"];
    adhaar_card = request.POST["adhaar_card"];
    city = request.POST["city"];
    country = request.POST["country"];
    mother_name = request.POST["mother"];
    father_name = request.POST["father"];
    email = request.POST["email"];
    mobile = request.POST["mobile"];
    pasword = request.POST["password"]

    register = Rregister(first_name=first_name,last_name=last_name,school_name=School_name,gender=gender,address=address,
                         birth=birth,adhaar_card=adhaar_card,city=city,country=country,mother_name=mother_name,father_name=father_name,
                         email=email,mobile_number=mobile,password=pasword)
    if(register.save()):
        user = User.objects.create_user(first_name, email, pasword)
        user.last_name = last_name
        if user.save() :
            login(request)



        return HttpResponse("save data")



def login(request):
    if request.method =="POST" and request.POST["username"] !="":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...

        return HttpResponse("login")
    else:

        return render(request,"login/login.html")


    
