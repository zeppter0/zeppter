from django.utils import timezone

from admin_dashboard.models import Book
from mytest.html import Html
from bs4 import BeautifulSoup

class Post(object):
    def __init__(self,data):
        self.data = data

    def Post(self):

        ht = Html(self.data)
        parsed_html = BeautifulSoup(self.data)
        frame = parsed_html.body.find('img', attrs={'class': 'story-banner'})



        if Book.objects.filter(book_title=ht.title()).count() < 1 :
            if frame:
                book = Book(book_title=ht.title(),
                            book_description=ht.description(),

                            book_data=ht.content(),
                            book_arrcat=[1],
                            book_rates=2,
                            publisher=1,
                            keyboard=ht.title(),
                            book_publish=False,
                            book_upload_date=timezone.now(),

                            book_catid=1,
                            book_commit_id=1)
                book.get_remote_image("https://hindistory.net"+ht.image())
                book.save()
                return print("save data")
            else:
                book = Book(book_title=ht.title(),
                            book_description=ht.description(),

                            book_data=ht.content(),
                            book_arrcat=[1],
                            book_rates=2,
                            publisher=1,
                            keyboard=ht.title(),
                            book_publish=False,
                            book_upload_date=timezone.now(),

                            book_catid=1,
                            book_commit_id=1)
                book.save()
                return print("not img")




        return