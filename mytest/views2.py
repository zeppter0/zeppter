import re

from django.utils import timezone
from django.views.generic import View
from bs4 import BeautifulSoup
import requests

from admin_dashboard.models import Category, Book

"""  response = request.get(url)

  if response.ok:
      soup = BeautifulSoup(response.text)

      loc = soup.find_all('loc')

      for lo in loc:

      """

from django.http import HttpResponse

#url2 = "https://www.hindihorrorstories.info/sitemap.xml"
url = "https://www.hindisahityadarpan.in/sitemap.xml"

class TopHindiStory(View):

    def get(self,request):
        #return HttpResponse("hello word")
          response = requests.get(url)

          if response.ok:
              soup = BeautifulSoup(response.text)

              loc = soup.find_all('loc')

              for lo in loc:
                  print(lo.text)
                  response2 = requests.get(lo.text)
                  if response2.ok:
                      sp = BeautifulSoup(response2.text)
                      loc2 = sp.find_all('loc')
                      for ld in loc2:
                          print(ld.text)


                          self.gettophindistory(ld.text)




      #return self.gettophindistory("https://www.hindihorrorstories.info/2021/05/bhootiya-railway-track-story-hindi.html")
    def gettophindistory(self,url2):


        response = requests.get(url2)
        if response.ok :
           cat = "hooror story"
           soup =  BeautifulSoup(response.text)
           caatid = []

           content = soup.find('div',{"class":"post hentry"})
           keybord = soup.find_all("a" ,{'rel': 'tag'})
           kbtext = ','.join(str(e.text) for e in keybord)



           title = content.find('h1',{'class':'post-title entry-title'}).text
           data = content.find('div',{'class': 'post-body-inner'})
           img = content.img

           #img = imgd.img
           for s in soup.select('img'):
               s.extract()
           for s in soup.select('div'):
               s.extract()

           cats = Category.objects.filter(cat_title=cat)
           if cats.count() < 1:
               catsave = Category(cat_title=cat)
               catsave.save()

               caatid.append(catsave.id)
           else:
               caatid.append(cats[0].id)

           books = Book.objects.filter(book_title=title)
           title2 = re.sub('[^A-Za-z0-9-/().&\' ]+', "", str(title))

           if books.count() < 1 :
               book = Book(
                   book_title=title,
                   book_description=data.text[:500],

                   book_data=str(data),
                   book_arrcat=caatid,
                   book_rates=2,
                   publisher=1,
                   keyboard=kbtext,
                   book_publish=True,
                   book_upload_date=timezone.now(),
                   book_url=url2.split('/')[-1],
                   book_catid=1,
                   book_commit_id=1
               )

               if img['src']:
                   book.get_remote_image(img['src'])

               book.save()


           return HttpResponse(str(img['src']))







