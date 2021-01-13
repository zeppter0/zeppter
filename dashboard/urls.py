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
from django.contrib import admin
from django.urls import path

from dashboard import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.dashboard,name="dashboard"),
   # path('dashboard',views.shows,name="shows"),
    path('cardlist/<int:catid>',views.cardpost,name="cardpost"),
    path('view',views.view,name="view"),
    path('<str:title>/<int:id>',views.shodata,name="content"),
    path('bookdata/<int:id>',views.bookdata,name="content"),
    path('pdf_show/<int:id>',views.pdf_show,name="pdf_show"),
    path("booklist/<int:id>",views.listview,name="listview"),
    path("mobile_home",views.mobile_home,name="mobile_home"),
    path("mobileload",views.mobile_home,name="mobile_load"),
    path("googled9d554441dd811fd.html",views.googled9d554441dd811fd ,name="google"),
    path("sitemap.xml", views.sitemap,name="sitemap"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
