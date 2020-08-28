from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment

# Create your views here.
def index(request):
    if request.method == "GET" and "postid" in request.GET:
        postid = request.GET['postid']
        name = request.GET['name']
        email =request.GET['email']
        comments = request.GET['comment']

        comment  = Comment(postid=postid,name=name,email=email,comment=comments)
        comment.save()

    
    return HttpResponse()
