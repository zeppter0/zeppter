from os import name
import re
import tempfile

from django.core import files
from django.utils import timezone
from django.views.generic import View
from bs4 import BeautifulSoup
import requests
import praw
from pathlib import Path
import time
from mytest.models import Reddit
from zeppter import settings

import pytumblr
vurls = "https://www.vedantcomputers.com/index.php?route=extension/feed/google_sitemap"

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
      if "position" in requet.GET:
          position = requet.GET['position']
          pf = Reddit.objects.filter(name="devan").update(position=int(position))
      dev = "devan"
      books = Book.objects.all()
      try:
          pod = Reddit.objects.get(name=dev)
      except Reddit.DoesNotExist:
          pod = Reddit(
              name=dev,
              position=0

          )
          pod.save()


      pd = Reddit.objects.filter(name=dev)
      position = pd.first().position





      print("devan :"+str(position))
      post = OTpost()

      while books.count() >position and True:
          book = books[position]

          post.reddit(book=book)
        #  post.tumblr(book=book)
          position += 1
          print(position)
          pd.update(position=position) 



          time.sleep(900)
      else:
         return HttpResponse("suceesful")






class OTpost():
      
       def reddit(self,book):
           subr = 'zeppter2'
           reddit = praw.Reddit(client_id="_Q2Ct9Pq_cq4rQ",
                                client_secret="dvCTDkB7JwLKO-BUcJYCSyFPtWpiWg",
                                password="Sorry9023@",
                                user_agent="testscript by u/fakebot3",
                                username="zeppter2",
                                refresh_token="964035758195-slRbr3DjtWEUMRWWke9XiuiIUJi98g"


                                )


           subreddit = reddit.subreddit(subr)

           title = book.book_title[:300]
           title2 = BeautifulSoup(title).text
           selftext = book.book_data
           descrption = BeautifulSoup(selftext).text[:2000]
           

           subreddit.submit(title2,selftext=descrption + "\n https://www.zeppter.com/content/" + book.book_url + "/")

       def tumblr(self,book):
           title = book.book_title
           title2 = BeautifulSoup(title).text
           selftext = book.book_description
           descrption = BeautifulSoup(selftext).text
           client.create_link('zeppter', title=title2,
                              url="https://www.zeppter.com/content/" + book.book_url + "/",
                              description=descrption)


class Vedantcomputers(View):
    def get_data(self, request,loc):


        getdata = loc
        print(loc)
        response = requests.get(getdata)
        url2 = BeautifulSoup(response.text)


        input_tag = url2.find(attrs={"id": "content"})
        brands = input_tag.find('div', {'class': 'brand-image product-manufacturer'})


        if brands:
            title = input_tag.find('div', {'class': 'title page-title'})

            discription = input_tag.find('div', {'class': "block-content expand-content"})
            if discription.find("table"):

                Specification = discription.table.prettify()
            else:
                Specification = ""

            brands = input_tag.find('div', {'class': 'brand-image product-manufacturer'})
            brand = brands.find("a").span

            model = input_tag.find('li', {'class': "product-model"}).span
            img = input_tag.find('div', {'class': "swiper-wrapper"}).findAll('img')
            imgs = []
            print("hjhghjkfghjv")
            cad = []
            cats = url2.find('ul', {'class': 'breadcrumb'})
            for cat in cats:
                ct = cat.string
                if ct:
                    cad.append(ct)
            csa = cad[:-1]
            urlsd = cad.pop()[0].replace(' ', "-")

            for imh in img:
                imgs.append(imh['src'].split('/')[-1])

            for div in discription.findAll('table'):
                div.extract()
            #  for imgd in img.find('div',{'div':'swiper-wrapper'}):
            #      imgs.append(imgd.img.src)
            #  print(imgs)

            caatid = []

            for cd in csa:
                cats = Category.objects.filter(cat_title=cd)
                if cats.count() < 1:
                    catsave = Category(cat_title=cd)
                    catsave.save()
                    caatid.append(catsave.id)
                else:
                    caatid.append(cats[0].id)

            product = Book.objects.filter(book_title=title.text)
            print(title)
            if product.count() < 1:
                book = Book(
                    book_title=title.text,
                    book_description=discription.prettify(),
                    book_image=imgs,

                    book_data=str(discription),
                    book_arrcat=caatid,
                    book_rates=2,
                    publisher=1,
                    keyboard="",
                    book_publish=True,
                    book_upload_date=timezone.now(),
                    book_url=title.text.replace(' ', "-"),

                    book_catid=1,
                    book_commit_id=1,
                    brand=brand.string,
                    model=model.string,
                    specifications=Specification
                )
                self.imgsave(imgs)

                book.save()





    #    div2 = input_tag.find(attrs={'id': 'product'})







    def post(self):
        response = requests.get(vurls)

        if response.ok:
            soup = BeautifulSoup(response.text)

            loc = soup.find_all('loc')

            for lo in loc:
                url2 = BeautifulSoup(lo.text)

                input_tag = url2.find(attrs={"id": "content"})
                div2 = input_tag.find(attrs={'id': 'product'})
                div3 = input_tag.find(attrs={'class': ''})

        return None


    def imgsave(self,ims):
        for url in ims:
            local_filename = url.split('/')[-1]
            local =settings.BASE_DIR+"/file/img/"

            r = requests.get(url)
            f = open(local + local_filename, 'wb')

            for chunk in r.iter_content(chunk_size=512 * 1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
            f.close()
    def get(self,request):
        url = requests.get(vurls)
        if url.status_code == 200:
            soup = BeautifulSoup(url.text)


            locs = soup.findAll("loc")
            for loc in locs:

                self.get_data(request,loc.string)





        return HttpResponse("susessuful")
















