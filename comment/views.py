from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment
import json
from myuser.models import MyUeers
# Create your views here.
def index(request):
    if request.method == "POST" and "postid" in request.POST:
        postid = request.POST['postid']
        name = request.POST['name']
        email =request.POST['email']
        comments = request.POST['comment']

        comment  = Comment(postid=postid,name=name,email=email,comment=comments)
        comment.save()

        username = comment.name
        data= {
            'name': comment.name,
            'comment': comment.comment,
            'response' : "sussecsful"

        }
        json_data =  json.dumps(data)

        return HttpResponse(json_data)



    
    return HttpResponse()
def comment(request):
    return HttpResponse("hello")


def send(request):
    error = "error"

    if "email" in request.session and request.method in "POST" and "userid" \
        in request.POST and "comment" in request.POST and "bookid" in request.POST:
        userid = request.POST['userid']

        user = MyUeers.objects.get(pk=int(userid))
        email = user.email


        comment = request.POST["comment"]
        bookid = request.POST["bookid"]



        if comment != "" and request.session["email"] == email:
            comment_d = Comment()
            comment_d.comment = comment
            comment_d.userid = int(userid)
            comment_d.contentid = int(bookid)
            comment_d.save()


            return render(request,"mobile/dashboard/load/commet.html",{"comment" : comment_d,"userdata" : user})
        error = "data"





    return HttpResponse(error)




def commentshow(request):


    
    return HttpResponse("hello word")