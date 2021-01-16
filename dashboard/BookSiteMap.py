from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from admin_dashboard.models import Book


class BookSiteMap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, item):
        return reverse(item)