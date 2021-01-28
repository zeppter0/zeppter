import urllib.request as re
from urllib.error import HTTPError, URLError

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from admin_dashboard.models import Book
from .form import NameForm
from bs4 import BeautifulSoup
from googletrans import Translator


from .html import Html
from .post import Post
import re

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
    s = ""
    if request.method in "GET":
        try:
            response = ur.urlopen(request.GET['url'])

            test = Html(response.read())
            text = test.list()
            s += str(text)


        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            print('Website is working fine')

        return HttpResponse(s)


    try:
        response = ur.urlopen("https://www.hindihorrorstories.info/")

        test = Html(response.read())
        text = test.list()
        s+=str(text)


    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print('Website is working fine')

    return HttpResponse(s)









 #   po = Post(s)
 #   po.Post()









    return HttpResponse()
def getResponseCode(url):
    conn = urllib.request.urlopen(url)
    return conn.getcode()


def modifalang(request):
    books = Book.objects.all()

    for d in books:
        df = re.sub("-+", " ", d.book_url)
        if d.book_url =="":
            dat = Book.objects.filter(id=d.id).update(keyboard=d.book_url[:15], book_url=d.book_url[:60].replace(" ", "-"))






    return HttpResponse("not change")

def changelang(request):
    s = ""
    books = Book.objects.all()

    for d in books:
        df = re.sub("-+"," ", d.book_url).rstrip().lstrip()


        if df == " " or d.book_url == "-" or d.book_url.rstrip().lstrip() == "":
            translator = Translator()
            trans1 = translator.translate(d.book_title, dest='en')



            data = re.sub(r"[^A-Za-z0-9 ]+", '', trans1.text)
            if trans1.text == "":
                dat = Book.objects.filter(id=d.id).update(keyboard=d.book_title[:15], book_url=d.book_title[:60].replace(" ", "-"))
            else:

                dat = Book.objects.filter(id=d.id).update(keyboard=data[:15], book_url=data[:60].replace(" ", "-"))

            print(data[:15])





    return HttpResponse("not change")




def update(request):

    books = Book.objects.all()

    for book in books:
        title = book.book_title.rstrip().lstrip().replace('\n', ' ').replace('\r', '')
        description = book.book_description.rstrip().lstrip().replace('\n', ' ').replace('\r', '')

        bookup = Book.objects.filter(id=book.id).update(book_title=re.sub(" +"," ",title),book_description=re.sub(" +"," ",description))

    return HttpResponse("sesses")
