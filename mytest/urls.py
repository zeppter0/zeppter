from django.urls import path

from mytest import views


urlpatterns = [
    path("",views.update,name="image_upload"),
]