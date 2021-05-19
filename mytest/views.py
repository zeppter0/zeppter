import urllib
import urllib.request as re
from os.path import join
from urllib import request
from urllib.error import HTTPError, URLError

import time,sched

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from django.views import View



from admin_dashboard.models import Book
from mytest.json import Post
from .form import NameForm
from bs4 import BeautifulSoup

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
web__url4 = "www.hindivibhag.com"
web__url2 = "hindi.storytal.com"
web__url5 = "homeremediesfast.com"
web__url50 = "www.merisaheli.com"
web__url6 = "www.achhikhabar.com"
web__url7 = "www.sarita.in"
web__url8 = "www.hindimein.in"
web__url9 = "www.hindibabu.com"
web__url10 = "happyhindi.com"
web__url11 = "www.sarassalil.in"
web__url12 = 'mauryamotivation.com'
web__url13 = 'motivational.page'
web__url14 = 'shortstoriesinhindi.com'
web__url15 = 'dhakadbaate.com'

web__url16 = 'www.hindikahane.in'
web__url17 = 'maskaree.com'

web__url18 = 'www.hindivarta.com'
web__url19 = 'epustakalay.com'
#web__url20 = 'http://www.hindibol.in'
web__url20 = 'www.paheliyaninhindi.in'
web__url21 = 'motivationalstoryinhindi.com'
web__url =horrorstorieshindi.com'


webarray = [web__ur3,web__url50,web__url2,web__url4,web__url5,web__url6,web__url7,web__url8,web__url9,web__url10,web__url11,web__url12,web__url13,web__url14,web__url15,web__url16,web__url17,web__url18,web__url19,web__url20,web__url21]
s = sched.scheduler(time.time, time.sleep)

def do_something(request):
    while True:
      for webv in webarray:

         wordpressjson('https://'+webv+'/wp-json/wp/v2/posts',webv)
         print(webv)
      else:     
           time.sleep(900) 


    
   # s.enter(21600, 1, do_something, (sc,))
    
    
    
    





def wordpress(request,id):
    for d in range(7):
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
           



            data = ""
            trans1 = ""
            if trans1 == "":
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
            trans1 = ''


            data = ""
            if trans1.text == "":
                dat = Book.objects.filter(id=d.id).update(keyboard=d.book_title[:15], book_url=d.book_title[:60].replace(" ", "-"))
            else:

                dat = Book.objects.filter(id=d.id).update(keyboard=data[:15], book_url=data[:60].replace(" ", "-"))

            





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


def wordpressjson(url,web):
    response = requests.get(url)

    if response.ok:
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
                caty = requests.get("https://"+web+"/wp-json/wp/v2/categories/" + str((ca)))
             #   print(caty.text)
                if caty.status_code == 200:
                  jsc = json.loads(caty.text)
                  catname = jsc['name']
                  cats = Category.objects.filter(cat_title=catname)
                  if cats.count() < 1:
                    catsave = Category(cat_title=catname)
                    catsave.save()

                    caatid.append(catsave.id)
                  else:
                    caatid.append(cats[0].id)
            featured_media = requests.get("https://"+web+"/wp-json/wp/v2/media/" + str(js['featured_media']))
            #featured_media  = requests.get(js["_links"]['wp:featuredmedia'][0]['href'])
            #print(featured_media.text)
            img_json = json.loads(featured_media.text)
         #   print(img)
           # img = js['featuredimage']
            books = Book.objects.filter(book_title=title)
            keybord = re.sub(r"[^A-Za-z0-9 ]+", '', title)
            slug = js['slug']
            fgh = re.sub(' +', ' ', slug.rstrip().lstrip().replace('\n', ' ').replace('\r', ''))
            focaskey = re.sub(r"[^A-Za-z0-9 ]+", '', fgh)
            urlsd = focaskey.replace(" ", "-").rstrip("-").lstrip("-")

          #  keysearch = '%20'.join(title.split()[:2])
          #  datad = requests.get("http://google.com/complete/search?output=toolbar&q=" + keysearch)

           # soupd = BeautifulSoup(datad.text)
           # d = soupd.findAll('suggestion')
           # data = ""
           # string = []

          #  for i in d:
         #       string.append(i['data'])
#
         #   print(",".join(string[:5]))






            

            if books.count() < 1 and js['status']=="publish"  :
                book = Book(
                    book_title=title,
                    book_description=description,

                    book_data=str(parsed_html),
                    book_arrcat=caatid,
                    book_rates=2,
                    publisher=1,
                    keyboard="",
                      book_publish=True,
                    book_upload_date=timezone.now(),
                    book_url=urlsd,

                    book_catid=1,
                    book_commit_id=1
                )

                try:


                   img = img_json['guid']['rendered']

                   book.get_remote_image(img)
                except KeyError:
                    print("no img")   



                book.save()
























  


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






    res = requests.get("https://storymirror.com/sitemap.xml")
    if res.status_code == 200:
        xml = res.text
        print("siteme")

        y = BeautifulSoup(xml)
        data = y.findAll("loc")
        for ds in data:
            res = requests.get(ds.get_text())

            if res.status_code == 200:
                print("text")
                xml = res.text

                y = BeautifulSoup(xml)
                data = y.findAll("loc")
                for ds in data:
                    res = requests.get(ds.get_text())
                    if res.status_code == 200:
                        print("hello")
                        xml = res.text

                        y = BeautifulSoup(xml)
                        data = y.findAll("loc")
                        for ds in data:
                            
                            try:
                                hindistory(request, ds.get_text())
                            except HTTPError as e:
                                 print('The server couldn\'t fulfill the request.')
                                 print('Error code: ', e.code)
                            except URLError as e:
                                 print('We failed to reach a server.')
                                 print('Reason: ', e.reason)
                            else:
                                 print('Website is working fine')


    return HttpResponse("sucesssfull")


class Dada(View):
    def get(self,request):
                res = requests.get("https://storymirror.com/sitemaps/poem.xml")

                if res.status_code == 200:
                    xml = res.text

                    y = BeautifulSoup(xml)
                    data = y.findAll("loc")
                    for ds in data:
                        res = requests.get(ds.get_text())
                        if res.status_code == 200:
                            xml = res.text

                            y = BeautifulSoup(xml)
                            data = y.findAll("loc")
                            for ds in data:

                                try:
                                    hindistory(request, ds.get_text())
                                except HTTPError as e:
                                    print('The server couldn\'t fulfill the request.')
                                    print('Error code: ', e.code)
                                except URLError as e:
                                    print('We failed to reach a server.')
                                    print('Reason: ', e.reason)
                                else:
                                    print('Website is working fine')

                return HttpResponse("sucesssfull")

            
            
            
            






def hindistory(request, url):
    bdf = Book.objects.all()

    if bdf.count() <40000:
        return HttpResponse("puh")
    data =""
    response = requests.get(url)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text)

        d = soup.find("div", attrs={'id': "main-row"})
        if d:
            titles = d.find('h2', attrs={'class': 'title-target text-left d-none d-sm-block'})
            title = titles.text
            print(title)

            content = d.find("div", attrs="content-container avoid-text-copy story")

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

            arraycat = d.findAll("a", {
                "class": 'badge badge-light badge-light-hover p-2 rounded-pill mr-1 mb-2 ga-track border border-danger'})

            for catd in arraycat:
                cat_check = Category.objects.filter(cat_title=catd.text)
                if cat_check.count() < 1:
                    cats = Category(cat_title=catd.text)
                    cats.save()
                    catarray.append(cats.pk)


                else:
                    catarray.append(cat_check.first().id)

                books = Book.objects.filter(book_title=title)

            description = soup.find("meta", attrs={'name': "description"})

            books = Book.objects.filter(book_title=title)
            img = soup.find("img", attrs={"class": 'rounded shadow-lg d-block'})
            catds = d.find('span', attrs={'class': 'col-sm-6 col-12'})

            catmain = catds.find("a", attrs={'class': 'ga-track'})
            for s in catmain.select('b'):
                s.extract()

            cts = Category.objects.filter(cat_title=str(catmain.text.replace(':', "")))
            if cts.count() < 1:
                ctd = Category(cat_title=str(catmain.text.replace(':', "")))
                ctd.save()
                catarray.append(ctd.id)
            else:
                catarray.append(cts[0].id)

            print(img.get('src'))

            if books.count() < 1 and d:
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
                        try:
                            book.get_remote_image(img.get('src'))
                            print(img.get('src'))
                        except:
                            print("error data")
                        else:
                            print("error data")

                book.save()






    

       

    return data
class UrlChange(View):
    def get(self,request):
        book = Book.objects.all()
        for b in book:
            bd = Book.objects.filter(id=b.id).update(book_url= b.book_url.replace("/",""))



        return HttpResponse("suscesssful")





class Google(View):
    def get(self, request):
        # <view logic>
        return render(request,'test/google/views.html')



class Webdunia(View):
    def get(self,request):
        urlrespose = requests.get("https://hindi.webdunia.com/sitemaps/recipe.xml")
        if urlrespose.status_code == 200:
            soup = BeautifulSoup(urlrespose.text)

            d = soup.find("div", attrs={'id': "main-row"})
            title = d.find("div", attrs={'class',"det_title"})
            #discription =


class Shyamvishwakarma(View):
    def get(self,request):
        url = requests.get("http://shyamvishwakarma.blogspot.com/sitemap.xml?page=1")
        if url.status_code == 200:
            soup = BeautifulSoup(url.text)

            locs = soup.findAll("loc")
            for loc in locs:
                print(loc)
                url2 = requests.get(loc)
                if url2.status_code == 200:
                    fullcontent = BeautifulSoup(url2.text).find("class", "post hentry uncustomized-post-template")


                    title = fullcontent.find("class","post-title entry-title")
                    content = fullcontent.find("class" "img")





