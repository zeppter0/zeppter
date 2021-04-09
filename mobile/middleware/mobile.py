
import re



class IS_MOBILE(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        device = self.mobile(request)
        request.device = device

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response




    def mobile(self, request):
        device = {}

        ua = request.META.get('HTTP_USER_AGENT', '').lower()

        if ua.find("iphone") > 0:
            device['iphone'] = "iphone" + re.search("iphone os (\d)", ua).groups(0)[0]

        if ua.find("ipad") > 0:
            device['ipad'] = "ipad"

        if ua.find("android") > 0:
            device['android'] = "android" + re.search("android (\d\.\d)", ua).groups(0)[0]

        # spits out device names for CSS targeting, to be applied to <html> or <body>.
        device['classes'] = " ".join(v for (k, v) in device.items())
        return {'device': device}




