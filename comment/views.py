from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment
from django.views.generic import View
import json
from myuser.models import MyUeers
# Create your views here.

class CommentPost(View):
    def post(self,request):
        if "postid" in request.POST and "email" in request.session:
            postid = request.POST['postid']

            comments = request.POST['comment']
            user = MyUeers.objects.get(email=request.session.get("email"))
            data = []

            if user:
                comment_d = Comment()
                comment_d.comment = comments
                comment_d.userid = user.pk
                comment_d.contentid = int(postid)
                comment_d.save()
                data = {
                    'name': user.first_name,
                    "photo" : user.photo,
                    'comment': comment_d.comment,
                    "usrid" : user.pk,
                    "date" :comment_d.pub_date,
                    "email" : user.email,
                    'response': "sussecsful"

                }






            return render(request,"dashboard/comment.html",{"comment": data})

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