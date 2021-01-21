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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from django.urls import path, include
from django.http import HttpResponse
from admin_dashboard.models import Book
from django.views.generic import TemplateView





urlpatterns = {
  #  path("admin/", admin.site.urls),
    path('hello/', include('admin_dashboard.urls')),
    path('', include('dashboard.urls')),
    path('json/', include('djson.urls')),
    path('comment', include('comment.urls')),
    path("test/", include("mytest.urls")),
    path("call/", include('videocall.urls')),
    path("mobile/", include("mobile.urls")),
    path("test", include("mytest.urls"), name="test"),
    # path("admin/<str:id>",include("plopleadmin.urls")),
     path("admin/",include("myuser.urls")),
    # path("robots.txt",views.robots ,name="roboot.txt"),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='include/robot.txt',
                                                content_type='text/plain')),
url('yandex_47dbe3c258eabd6f.html', TemplateView.as_view(template_name='include/yandex_47dbe3c258eabd6f.html',
                                                content_type='text/plain')),
    url('BingSiteAuth.xml',TemplateView.as_view(template_name='include/BingSiteAuth.xml',
                                                content_type='text/plain')),


}

