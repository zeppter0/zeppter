from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myuser.models import MyUeers
# Create your views here.
def login(request):
    if "email" in request.session:
        user = request.session["email"]

        data = {
            "data": user,
        }

        return HttpResponseRedirect('welcome')
    elif request.method == 'POST' and 'email' in request.POST and 'password' in request.POST:
        username = request.POST["email"]
        user = MyUeers.objects.filter(email=username)
        if user.count() == 1:
            clearPassNoHash = request.POST['password']

            checkd = check_password(clearPassNoHash, user[0].password)

            if checkd and username == user[0].email:
                ud = request.session["email"] = username
                return HttpResponseRedirect('welcome')
            else:
                return render(request,'login/login.html',{'error': "password is wrong"})











        else:

            username = "insert user"

            return render(request, 'login/login.html', {"error": "wrong email"})

    else:
        return render(request,'login/login.html')




def welcome(request):

    if 'email' in request.session:
        email = request.session['email']
        user = MyUeers.objects.filter(email=email)
        return render(request, 'login/welcome.html',{"data":user} )
    else:
        return HttpResponseRedirect("login")



def logout(request):
    del request.session['email']

    return HttpResponseRedirect("login")





def Register(request):

    if 'email' in request.session :
        return HttpResponseRedirect('welcome')

    elif request.method in "POST" and  'email' \
            in request.POST and 'first_name' \
            in request.POST and 'last_name' \
            in request.POST and 'mobile_no'\
            in request.POST and 'gender'\
            in request.POST and "password1"\
            in request.POST and "password2":


        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_no = request.POST['mobile_no']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        pass4 = make_password(password1)
        if password1 ==password2 :
            myuser = MyUeers.objects.filter(email=email)
            if myuser.count() <1:
                user = MyUeers(gender=gender, first_name=first_name,
                               last_name=last_name, email=email, password=pass4, mobile_no=int(mobile_no))
                user.save()
                request.session['email'] = email
                return HttpResponseRedirect('welcome')
            else:
                return render(request,'login/register.html',{'error': "all ready email"})
        else:
            return render(request,'login/register.html',{'error': "not match the password"})
    else:





        return render(request,'login/register.html',{'error': "please insert data"})

