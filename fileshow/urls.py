from django.urls import path

from fileshow import views

urlpatterns = [
    path('img/<str:url>',views.Img.as_view()),

]