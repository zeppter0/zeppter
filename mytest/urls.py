from django.urls import path

from mytest import views


urlpatterns = [
    path("<int:id>",views.changelang,name="image_upload"),
]