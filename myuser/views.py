from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myuser.models import MyUeers
# Create your views here.
def login(request):
    if "usernaame" in request.session:
        user = request.session["usernaame"]

        data = {
            "username": user,
        }

        return render(request,"welcome.html",data)
    else:


        if request.method == 'POST':
            username = request.POST["email"]
            user = MyUeers.objects.filter(email=username)


            clearPassNoHash = request.POST['pass']
            password = make_password(clearPassNoHash, None, 'md5')
            checkd = check_password(clearPassNoHash,user)

            if checkd:
                ud = request.session["usernaame"] = username
                return render(request, 'login.html', {"username": ud, "clearPassNoHash": password})
            else:
                return HttpResponse(clearPassNoHash)


        else:

            username = "insert user"

            return render(request, 'login.html', {"username": username})






def logout(request):
    del request.session['usernaame']

    return HttpResponseRedirect("login")


def Register(request):
    if request.method in "POSt":
        return
    return render(request,"login/register.html")
