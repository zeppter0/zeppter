from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from myuser.models import MyUeers


class BookSiteMap(Sitemap):


    def items(self):
        return MyUeers.objects.all()


    def location(self, item):
        return reverse('content/'+item.book_url+'/')