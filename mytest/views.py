from sys import addaudithook
import urllib
import urllib.request as re
from os.path import join
from urllib import request
from urllib.error import HTTPError, URLError
import translate

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from googletrans import Translator, LANGUAGES
from googletrans.models import Translated
from googletrans import Translator


from admin_dashboard.models import Book
from mytest.json import Post
from .form import NameForm
from bs4 import BeautifulSoup
from googletrans import Translator
from django.core import serializers
from admin_dashboard.models import Category
import requests

from .html import Html
from .post import Post
import re

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
# Create your views here.
import json

import urllib.request as ur
web__ur3 = "www.grihshobha.in"
web__url2 = "thatsmystory-book.com"
web__url = "www.hindikahane.in"

def wordpress(request,id):
    for d in range(11):
        wordpressjson('https://'+web__url+'/wp-json/wp/v2/posts?page='+str(id+d))
        print(id+d)
    return HttpResponse("hello word")
def changecatgory(request):
    books = Book.objects.all()
    for book in books:
        if book.book_catid != 1:
            bd = Book.objects.filter(id=book.id)
            bd.update(book_arrcat=[book.book_catid])
    return HttpResponse("sesse")

def keyboardserach(request):
    books = Book.objects.all()
    for book in books:


        title = book.book_title
        keysearch = '%20'.join(title.split()[:3])
        data =   requests.get("http://google.com/complete/search?output=toolbar&q="+keysearch)


        xmlse = BeautifulSoup(data.text)
        jsdata = []


        for d in xmlse.findAll("suggestion"):
            jsdata.append(d['data'])


        bks = Book.objects.filter(pk=book.pk)
      #  bks.update(keyboard="hello")

      #  print(",".join(jsdata[:5]))
        bks.update(keyboard=",".join(jsdata[:5]))

        print(",".join(jsdata[:5]))
    return HttpResponse("sussec")









def imageupload(request):
    #  html = re.urlopen("https://www.livehindustan.com/nandan/story-old-book-3136666.html")
  # sl = ur.urlopen("https://hindistory.net/story/555" )
  #  s = sl.read()
  ##  po = Post(s)
  #  po.Post()
    s = ""
    if request.method in "GET":

        wordpressjson(request.GET['url'])

        return HttpResponse(s)












 #   po = Post(s)
 #   po.Post()










def  books(request):
    books = Book.objects.all()
    serialized_queryset = serializers.serialize('json', books)
    return HttpResponse(serialized_queryset)





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
    books = Book.objects.all().order_by('-id')

    for d in books:
        df = re.sub("-+"," ", d.book_url)


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


def check(request):
    data= ""
    books = Book.objects.all()
    for d in books:

        return HttpResponse(str(d.book_arrcat))

def changebook(request,book):
    s = ""
    books = Book.objects.filter(book_url=book)

    for d in books:
        df = re.sub("-+"," ", d.book_url)


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




def geturl(data):

    s = ""
    try:
        response = ur.urlopen(data)
        s = response.read()
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print('Website is working fine')
    return s


def wordpressjson(url):
    try:
        response = ur.urlopen(url)
     #   response = requests.get(url)

        jas = json.loads(response.text)
        caatid = []
        for js in jas:
            title = js['title']['rendered']
            content = js['content']['rendered']
            parsed_html = BeautifulSoup(content)
            for f in parsed_html.select('img'):
                f.extract()

            for f in parsed_html.select('a'):
                f.extract()
            for f in parsed_html.select('script'):
                f.extract()
            description = parsed_html.text[:400]
            cat = js['categories']
            for ca in cat:
                caty = geturl("https://"+web__url+"/wp-json/wp/v2/categories/" + str((ca)))
                jsc = json.loads(caty)
                catname = jsc['name']
                cats = Category.objects.filter(cat_title=catname)
                if cats.count() < 1:
                    catsave = Category(cat_title=catname)
                    catsave.save()

                    caatid.append(catsave.id)
                else:
                    caatid.append(cats[0].id)
            featured_media = geturl("https://"+web__url+"/wp-json/wp/v2/media/" + str(js['featured_media']))
            img_json = json.loads(featured_media)
            img = img_json['guid']['rendered']
           # img = js['featuredimage']
            books = Book.objects.filter(book_title=title)
            keybord = re.sub(r"[^A-Za-z0-9 ]+", '', title)
            slug = js['slug']
            fgh = re.sub(' +', ' ', slug.rstrip().lstrip().replace('\n', ' ').replace('\r', ''))
            focaskey = re.sub(r"[^A-Za-z0-9 ]+", '', fgh)
            urlsd = focaskey.replace(" ", "-").rstrip("-").lstrip("-")

            keysearch = '%20'.join(title.split()[:3])
            datad = requests.get("http://google.com/complete/search?output=toolbar&q=" + keysearch)

            soupd = BeautifulSoup(datad.text)
            d = soupd.findAll('suggestion')
            data = ""
            string = []

            for i in d:
                string.append(i['data'])

            print(",".join(string[:5]))






            if img == "":
                return print('notimg')

            if books.count() < 1 and js['status']=="publish" and datad.status_code == 200 and img.find(web__url) >= 0:
                book = Book(
                    book_title=title,
                    book_description=description,

                    book_data=str(parsed_html),
                    book_arrcat=caatid,
                    book_rates=2,
                    publisher=1,
                    keyboard=",".join(string[:5]),
                    book_publish=True,
                    book_upload_date=timezone.now(),
                    book_url=urlsd,

                    book_catid=1,
                    book_commit_id=1
                )
                book.get_remote_image(img)



                book.save()
























    #   test = Html(response.read())
    #  text = test.list()
    #    s += str(text)

    #   post.json()

    #  return JsonResponse(response.read())

    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print('Website is working fine')

    return "load susecuss"


def keyboad(title):
    keysearch = keysearch = '%20'.join(title.split()[:3])
    data = requests.get("http://google.com/complete/search?output=toolbar&q=" + keysearch)

    soup = BeautifulSoup(data.text)
    d = soup.findAll('suggestion')
    data = ""
    string = []

    for i in d:
        string.append(i['data'])

    print(",".join(string[:5]))

    return ",".join(string[:5])


def urldata(request):




    res = requests.get("https://storymirror.com/sitemaps/story/hindi.xml")
    if res.status_code == 200:
        xml = res.text

        y = BeautifulSoup(xml)
        data = y.findAll("loc")
        for ds in data:
            hindistory(request,ds.get_text())
            
            
            
            






def hindistory(request, url):
    data =""
    response = requests.get(url)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text)
        d = soup.find("div", attrs={'id': "main-row"})

        titles = d.find('h2', attrs={'class': 'title-target text-left d-none d-sm-block'})
        title = titles.text
        print(title)

        content = d.find("div",attrs="content-container avoid-text-copy story")



        url = re.sub("^a-zA-Z\u0900-\u097F+", '', title)

        keysearch = '%20'.join(title.split()[:3])
        datad = requests.get("http://google.com/complete/search?output=toolbar&q=" + keysearch)

        soupd = BeautifulSoup(datad.text)
        ds = soupd.findAll('suggestion')
        data = ""
        string = []



        for i in ds:
            string.append(i['data'])

        print(",".join(string[:5]))
        catarray = []

        arraycat = d.findAll("a", {"class": 'badge badge-light badge-light-hover p-2 rounded-pill mr-1 mb-2 ga-track border border-danger'})

        for catd in arraycat:
            cat_check = Category.objects.filter(cat_title=catd.text)
            if cat_check.count() < 1:
                cats = Category(cat_title=catd.text)
                cats.save()
                catarray.append(cats.pk)


            else:
                catarray.append(cat_check.first().id)

            books = Book.objects.filter(book_title=title)

        catid = 1
        description = soup.find("meta" ,attrs={'name':"description"})

        cat_check = Category.objects.filter(cat_title="hindi story")
        if cat_check.count() < 1:
            catr = Category(cat_title="hindi story")
            catr.save()
            catid = catr.id

        else:
            catid = cat_check.first().id

        books = Book.objects.filter(book_title=title)
        img = soup.find("img", attrs={"class": 'rounded shadow-lg d-block'})
        print(img.get('src'))


        if books.count() < 1:
            book = Book(
                book_title=title,
                book_description=str(description['content']),

                book_data=str(content),
                book_arrcat=catarray,
                book_rates=2,
                publisher=1,
                keyboard=",".join(string[:5]),
                book_publish=True,
                book_upload_date=timezone.now(),
                book_url=url.replace("\n", "").replace(" ", "-"),

                book_catid=1,
                book_commit_id=1
            )




            if img:
                check_img = requests.get(img.get('src'))
                if check_img.status_code == 200:
                   book.get_remote_image(img.get('src'))
                   print(img.get('src'))




            book.save()



    

       

    return data
