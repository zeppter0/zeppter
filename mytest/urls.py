from django.urls import path

from mytest import views


urlpatterns = [
    path("",views.changelang,name="image_upload"),
]