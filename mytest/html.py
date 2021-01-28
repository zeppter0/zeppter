import re

from bs4 import BeautifulSoup

from urllib.error import HTTPError, URLError
import urllib.request as ur

from admin_dashboard.models import Book
from mytest.post import Post


class Html(object):
    TITLE = ""
    DESCRIPTION = ""
    CONTENT = ""

    def __init__(self,html):
        self.html = html


    def list(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.findAll('div', attrs={'class': 'post-outer'})

        for d in frame:
            print(d.a['href'])

            self.content(d.a['href'])







        return frame




    def content(self=None,urld=""):
        s = ""

        try:
            response = ur.urlopen(urld)
            html = BeautifulSoup(response.read())
            img = html.find('link',attrs={'rel' : "image_src"})

            title = html.body.find('h1',attrs={'class' : "post-title entry-title"} )
            content = html.body.find('div', attrs={'class': 'post-body entry-content'})
            for f in content.select('span'):
                f.extract()
            for f in content.select('a'):
                f.extract()
            for f in content.select('img'):
                f.extract()

            data =""
            df = Post(data)
           # print(title.text)


            df.newPost(img['href'],title.text,content.text)







        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            print('Website is working fine')



        return None
    def htmlcontent(data):
        html = BeautifulSoup(data)
        title = html.body.find('h2', attrs={'class': 'post-title entry-title'})
        print(title)





    def is_image(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.find('div', attrs={'class': 'col-md-9 col-md-push-3'})
        for f in frame.select('h1'):
            f.extract()
        for f in frame.select('p'):
            f.extract()

        for f in frame.select('h3'):
            f.extract()

        for f in frame.select('div', ):
            f.extract()



        return frame.img.name








