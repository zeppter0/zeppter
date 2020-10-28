from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment
import json

# Create your views here.
def index(request):
    if request.method == "POST" and "postid" in request.POST:
        postid = request.POST['postid']
        name = request.POST['name']
        email =request.POST['email']
        comments = request.POST['comment']

        comment  = Comment(postid=postid,name=name,email=email,comment=comments)
       # comment.save()

        username = comment.name
        data= {
            'name': comment.name,
            'comment': comment.comment,
            'response' : "sussecsful"

        }
        json_data =  json.dumps(data)

        return HttpResponse(json_data)



    
    return HttpResponse()
