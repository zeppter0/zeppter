from django.urls import path
from myuser.models import MyUeers
from myuser import views
from django.contrib.sitemaps.views import sitemap
sitemaps =  {"book" : MyUeers()

             }

urlpatterns = [
    path("register",views.Register,name="register"),
    path("login",views.login,name="login"),
    path('welcome',views.welcome ,name="welcome"),
    path('logout',views.logout ,name="logout"),
    path("photo/<int:id>",views.photoupload,name="photo_upload"),
    path("data/name/<int:id>",views.changedata,name="changedata"),
path("sitemap.xml", views.sitemap, name="sitemap"),


]