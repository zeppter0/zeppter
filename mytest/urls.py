from django.urls import path

from mytest import views


urlpatterns = [
    path("",views.imageupload,name="image_upload"),
   path("change/<int:id>",views.wordpress,name="change_url"),
path("change/<str:book>",views.changebook,name="change_url"),
path("check",views.check,name="check"),
   path('books',views.books,name="books"),
path('changecat',views.changecatgory,name="changecatgory"),
]