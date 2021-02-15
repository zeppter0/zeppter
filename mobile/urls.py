from django.urls import path
from django.views.generic import RedirectView


from mobile import views
from django.contrib.sitemaps.views import sitemap

from mobile.MobileSitemap import MobileSitemap

sitemaps =  {"book" : MobileSitemap()}


urlpatterns = [
    path("content/<str:url>/",views.content,name="content"),
    path("content/<str:url>",views.content,name="content"),

    path("mobile_pdf/<int:id>",views.showdatapdf, name="iul"),
    path("mobilecard/<int:id>",views.mobilecard, name="showpdf"),
    path("home",views.home,name="mobilehome"),
    path("content/<str:url>/mobileload",views.content,name="contentload"),
    path("search",views.search,name="mobile_serach"),
    path("listview/<int:cat>/mobileload",views.listview,name="listview"),
path("listview/<int:cat>/",views.listview,name="listview"),
    path('sitemap.xml', views.sitemap ,name="mobile_site"),
    path('login', views.login ,name="login_mobile"),
    path('register', views.register ,name="register_mobile"),
    path('user/data/<int:id>',views.userprofile,name="user_profile"),
]