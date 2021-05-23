import re
import tempfile

from django.core import files
from django.utils import timezone
from django.views.generic import View
from bs4 import BeautifulSoup
import requests
import praw
import time

import pytumblr

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



client = pytumblr.TumblrRestClient(
  's4v0FXPgXKcCswCfpCRNJyF5D8RSOAv4DU0nQUoRgJ7BpHNWoC',
  'fwlUxcIvVtynb611Ys7VANm2XFEyJVANzWZTykpNDSTIGnNwOv',
  'B48jqNK64PaO4huou53avOGXRLG5Uq1alqS1re1iPtogS4d5mJ',
  'VRq5Tgznx7Qt3HtiKdQeHC3PbS7wvyjX6xLIuCCmJRpp8GbsDk'
)


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


        global img
        response = requests.get(url2)
        if response.ok :
           cat = "hooror story"
           soup =  BeautifulSoup(response.text)
           caatid = []

           content = soup.find('body')
           keybord = soup.find_all("a" ,{'rel': 'tag'})
           kbtext = ','.join(str(e.text) for e in keybord)



           title = soup.find('h1',{'class':'post-title entry-title'}).text
           data = content.find('div',{'class': 'MsoNormal'})
           imh = soup.find('div',{'class' : 'post-feature-image-wrapper'})
           if imh :
              img = imh.img

           #img = imgd.img
         #  for s in data.select('img'):
         #      s.extract()
          # for s in data.select('div'):
          #     s.extract()

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
                   book_description=data[:500],

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
               try:

                if img :
                   book.get_remote_image(img['src'])


               except NameError:
                 print("not img")

               book.save()
           else:
               books.update(
                   book_title=title,
                   book_description=data,

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


           return HttpResponse("sow")



    def update_remote_image(self, image_url):

        image_save = requests.get(image_url, stream=True)
        if image_save.ok:

            file_name = image_url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in image_save.iter_content(1024 * 8):

                # If no more file then stop
                if not block:
                    break

                lf.write(block)
            self.book_image.save(file_name, files.File(lf))
            self.update()



class Tumblr(View):
    def get(self,request):
        books = Book.objects.all()
        for book in books:

          client.create_link('zeppter', title=book.book_title, url="https://www.zeppter.com/content/"+book.book_url+"/",
                   description=book.book_description)

          print(client.info())

        return HttpResponse("post sussessfull")




class Reddits(View):
   def get(self,requet):
      books = Book.objects.all()

    #  position = int(rd.select("devan"))

      while len(books) <33000:
          position = 1

          subr = 'zeppter'
          reddit = praw.Reddit(client_id="C3L3EVrFp8KxUw",
                               client_secret="nM3YOeSTOQ9L8HcFj6hDgkuh6EQlTw",
                               password="Sorry9023@",
                               user_agent="testscript by u/fakebot3",
                               username="zeppter0",
                               refresh_token='962000230191-ET0KhOP6sjAXaagMKXuiqFDcBf_DRg'

                               )

          subreddit = reddit.subreddit(subr)

          title = books[position].book_title
          selftext = books[position].book_description

          subreddit.submit(title, selftext=selftext+"\n https://www.zeppter.com/content/"+books[position].book_url+"/")
          time.sleep(350)
      else:
         return HttpResponse("suceesful")
