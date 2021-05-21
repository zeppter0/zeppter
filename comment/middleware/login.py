
from comment.models import Comment
from myuser.models import MyUeers
from django.http import HttpResponseRedirect,HttpResponse
class Login:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if "email" in request.session and 'userid' in request.POST:
            email = request.session.email
            userid = request.POST['userid']
          #  comment = Comment.objects.get(pk=id)
            user_email = MyUeers.objects.get(pk=userid)

            if email == user_email.email:







                 response = self.get_response(request)
                 return response
        return  HttpResponse("wrong data insert")

        # Code to be executed for each request/response after
        # the view is called.

