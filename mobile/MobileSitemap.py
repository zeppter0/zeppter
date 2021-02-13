
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from admin_dashboard.models import Book


class MobileSitemap(Sitemap):

    def items(self):
        return Book.objects.all()

    def location(self, item):
        return reverse('content', args=(item.book_url,))