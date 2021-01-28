from django.urls import path

from mytest import views


urlpatterns = [
    path("",views.modifalang,name="image_upload"),
]