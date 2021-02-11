from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from admin_dashboard.models import Book


class BookSiteMap(Sitemap):


    def items(self):
        return Book.objects.all()






