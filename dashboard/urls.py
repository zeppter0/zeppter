"""zeppter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime

from django.contrib.sitemaps import views as st
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, register_converter

from admin_dashboard.models import Book
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static
from dashboard.BookSiteMap import BookSiteMap


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

sitemaps =  {"book" : BookSiteMap()

             }
urlpatterns = [

    path('', views.dashboard, name="dashboard"),
    # path('dashboard',views.shows,name="shows"),
    path('cardlist/<int:catid>', views.cardpost, name="cardpost"),
    path('view', views.view, name="view"),
    path('content/<str:url>', views.shodata, name="content"),
path('content/<str:url>/', views.shodata, name="content"),
    path('bookdatas/<int:id>', views.bookdata, name="content"),
    path('pdf_show/<str:url>', views.pdf_show, name="pdf_show"),
    path("booklist/<int:id>", views.listview, name="listview"),
    path("mobile_home", views.mobile_home, name="mobile_home"),
    path("mobileload", views.mobile_home, name="mobile_load"),
    path("contact",views.contect,name="content"),
    path("user/data/<int:id>",views.user_profile,name="user_profile"),
path("about", views.about,name="about"),
path("search", views.morelist, name="listview"),
    path("catlist/<int:id>",views.catlist,name="catlist"),

    path("googled9d554441dd811fd.html", views.googled9d554441dd811fd, name="google"),
   # url('sitemap.xml',views.sitema, name='django.contrib.sitemaps.views.sitemap')


    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')



    # path("robots.txt",views.robots ,name="roboot.txt"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
