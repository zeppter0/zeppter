from django.utils import timezone
from googletrans import Translator

from admin_dashboard.models import Book

from bs4 import BeautifulSoup
import re

class Post(object):
    def __init__(self,data):
        self.data = data

    def newPost(self,img,mtitle,content):

        title = re.sub(' +', ' ', mtitle.rstrip().lstrip().replace('\n', ' ').replace('\r', ''))
        focaskey = re.sub(r"[^A-Za-z0-9 ]+", '', title)
        urls = focaskey.replace(" ","-").rstrip("-").lstrip("-")
        if urls == "":
            translator = Translator()
            trans1 = translator.translate(title, dest='en')

            urls = re.sub(r"[^A-Za-z0-9 ]+", '', trans1.text)


        if Book.objects.filter(book_title=title).count() <1 :
            if img != "":
                book = Book(book_title=title,
                            book_description=content[:400],

                            book_data=content,
                            book_arrcat=[1],
                            book_rates=2,
                            publisher=1,
                            keyboard=focaskey,
                            book_publish=True,
                            book_upload_date=timezone.now(),
                            book_url=urls,

                            book_catid=1,
                            book_commit_id=1)
                book.get_remote_image(img)

                book.save()
                return print("save data")
            else:
                book = Book(book_title=title,
                            book_description=content[:400],

                            book_data=content,
                            book_arrcat=[1],
                            book_rates=2,
                            publisher=1,
                            keyboard=title,
                            book_publish=True,
                            book_upload_date=timezone.now(),

                            book_catid=1,
                            book_commit_id=1)
                book.save()
                return print("not img")

