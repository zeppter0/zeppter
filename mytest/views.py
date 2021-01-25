import urllib.request as re
from urllib.error import HTTPError, URLError

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import NameForm
from bs4 import BeautifulSoup

from .html import Html
from .post import Post

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
# Create your views here.
import urllib.request
import urllib.request as ur


def imageupload(request):
    #  html = re.urlopen("https://www.livehindustan.com/nandan/story-old-book-3136666.html")
  # sl = ur.urlopen("https://hindistory.net/story/555" )
  #  s = sl.read()
  ##  po = Post(s)
  #  po.Post()


    for k in range(1232):

        try:
            response = ur.urlopen("https://hindistory.net/story/"+str(k))
            s = response.read()
            po = Post(s)
            po.Post()

        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            print('Website is working fine')







 #   po = Post(s)
 #   po.Post()









    return HttpResponse()
def getResponseCode(url):
    conn = urllib.request.urlopen(url)
    return conn.getcode()
