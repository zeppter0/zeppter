from django.urls import path

from mytest import views


urlpatterns = [
    path("",views.imageupload,name="image_upload"),
]