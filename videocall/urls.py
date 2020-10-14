from django.urls import path

from videocall import views

urlpatterns = [
    path('',views.data ,name="index"),
    path('data',views.uploaddata, name="data")
]