from django.urls import path

from mytest import views,views2




urlpatterns = [
    path("",views.Google.as_view(),name="image_upload"),
   path("change/<int:id>",views.wordpress,name="change_url"),
path("change/<str:book>",views.changebook,name="change_url"),
path("check",views.check,name="check"),
   path('books',views.books,name="books"),
path('changecat',views.changecatgory,name="changecatgory"),
    path('searchkey' , views.keyboardserach,name="search"),
    path("posts",views.urldata,name="post"),
    path("changeurl",views.UrlChange.as_view()),
    path('getpostdata',views.Dada.as_view()),
    path("9023/update",views.do_something,name='update'),
    path('google',views2.TopHindiStory.as_view()),
    path('thumblr',views2.Tumblr.as_view()),
    path('reddit',views2.Reddits.as_view()),
    path('vurl',views2.Vedantcomputers.as_view()),
]