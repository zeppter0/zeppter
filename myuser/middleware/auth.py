from myuser.models import MyUeers

class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if 'email' in request.session:


            user = MyUeers.objects.get(email=request.session['email'])
            request.myuser = user


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response